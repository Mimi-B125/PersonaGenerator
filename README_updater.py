# 1. Capture the current directory tree structure
$treeOutput = Get-ChildItem -Path . -Exclude ".git", "__pycache__", "*.pyc" | ForEach-Object {
    if ($_.PSIsContainer) {
        "├── $($_.Name)/"
    } else {
        "├── $($_.Name)"
    }
} | Out-String

# 2. Read existing README.md
$readmePath = "README.md"
$readmeContent = Get-Content$readmePath -Raw

# 3. Replace the Repository Directory Structure section dynamically
$pattern = "(?s)```text\r?\nPersonaGenerator/.*?\r?\n```"
$newTree = "```text`nPersonaGenerator/`n$treeOutput```"

if ($readmeContent -match $pattern) {
    $updatedReadme = $readmeContent -replace $pattern, $newTree
    Set-Content -Path $readmePath -Value $updatedReadme
    Write-Host "README.md Directory Structure updated successfully!" -ForegroundColor Green
} else {
    Write-Host "Could not locate Directory Structure section in README.md." -ForegroundColor Yellow
}