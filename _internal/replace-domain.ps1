param(
  [Parameter(Mandatory = $true)]
  [string]$Domain
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$normalized = $Domain.Trim()
if (-not $normalized.StartsWith("http://") -and -not $normalized.StartsWith("https://")) {
  $normalized = "https://$normalized"
}
$normalized = $normalized.TrimEnd("/")

$files = @(
  "index.html",
  "articles/employee-equity-incentive.html",
  "robots.txt",
  "sitemap.xml",
  "llms.txt"
)

foreach ($file in $files) {
  $path = Join-Path $root $file
  $content = Get-Content -Raw -Encoding UTF8 -Path $path
  $content = $content.Replace("https://example.com", $normalized)
  Set-Content -Encoding UTF8 -Path $path -Value $content
}

Write-Host "已替换为正式域名：$normalized"

