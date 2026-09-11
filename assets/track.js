/* 轻量事件埋点（wltrack）
 * 设计约束：
 * 1) 不自动加载任何第三方统计 SDK，不向任何外部地址发送数据；
 * 2) 事件只记录页面、入口位置、需求类别、来源等一般营销维度；
 * 3) 任何疑似个人信息（域名、邮箱、手机号、案件编号、长数字）一律拒绝记录；
 * 4) 如需接入统计服务，由站点维护者在页面中显式配置 window.WL_ANALYTICS = { endpoint: '...' }，
 *    本脚本再通过 sendBeacon 转发，未配置时数据仅留在内存数组 window.__wlEvents 中（刷新即清空）。
 */
(function () {
  window.__wlEvents = window.__wlEvents || [];

  // 允许的事件名（白名单）
  var ALLOWED_EVENTS = {
    udrp_page_view: 1,
    udrp_need_select: 1,
    udrp_contact_click: 1,
    udrp_intake_open: 1,
    udrp_intake_generated: 1,
    udrp_intake_mail: 1,
    udrp_article_service_click: 1
  };

  // 允许的参数键（白名单）
  var ALLOWED_KEYS = {
    page: 1,
    need: 1,
    position: 1,
    channel: 1,
    source: 1,
    landing: 1
  };

  // 禁止出现的隐私/敏感模式
  var DENY_PATTERNS = [
    /\b\d{11}\b/,                                                            // 手机号
    /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/,                       // 邮箱
    /\b(?:[a-z0-9-]+\.)+(?:com|cn|net|org|ai|io|co|top|xyz|shop|site|info|biz|me|tv|cc|app|dev|cloud)\b/i, // 域名
    /\bD(?:19|20)\d{2}-\d{4}\b/i,                                            // WIPO 案号
    /\bFA\d{8,}\b/i,                                                         // FORUM 案号
    /\b\d{9,}\b/                                                             // 其他长数字串
  ];

  function isClean(value) {
    if (typeof value !== 'string') return true;
    if (value.length > 60) return false;
    for (var i = 0; i < DENY_PATTERNS.length; i++) {
      if (DENY_PATTERNS[i].test(value)) return false;
    }
    return true;
  }

  function sanitize(params) {
    var out = {};
    if (!params || typeof params !== 'object') return out;
    Object.keys(params).forEach(function (k) {
      if (!ALLOWED_KEYS[k]) return;
      var v = params[k];
      if (v === null || v === undefined) return;
      if (typeof v === 'number' || typeof v === 'boolean') { out[k] = v; return; }
      if (typeof v === 'string') {
        if (!isClean(v)) return;
        out[k] = v.slice(0, 60);
      }
    });
    return out;
  }

  /**
   * 记录一个事件。
   * @param {string} event 事件名（须在白名单内）
   * @param {object} params 参数（仅白名单键会被记录）
   */
  window.wlTrack = function (event, params) {
    try {
      if (!ALLOWED_EVENTS[event]) return;
      var payload = sanitize(params);
      payload.event = event;
      payload.ts = new Date().toISOString();
      window.__wlEvents.push(payload);

      var cfg = window.WL_ANALYTICS;
      if (cfg && typeof cfg.endpoint === 'string' && cfg.endpoint) {
        var body = JSON.stringify(payload);
        if (navigator.sendBeacon) {
          navigator.sendBeacon(cfg.endpoint, body);
        } else if (window.fetch) {
          fetch(cfg.endpoint, { method: 'POST', body: body, keepalive: true, headers: { 'Content-Type': 'application/json' } });
        }
      }
    } catch (e) {
      /* 埋点失败不影响页面功能 */
    }
  };

  // 自动记录一次页面访问（仅记录页面标识与来源，不含任何查询参数内容）
  // 页面内联脚本若已自行记录 udrp_page_view（可带上 need 等维度），这里不再重复记录。
  try {
    setTimeout(function () {
      var recorded = window.__wlEvents.some(function (e) { return e.event === 'udrp_page_view'; });
      if (recorded) return;
      var path = location.pathname.replace(/\/index\.html$/, '/');
      wlTrack('udrp_page_view', { page: path, source: document.referrer ? 'referral' : 'direct' });
    }, 0);
  } catch (e) {}
})();
