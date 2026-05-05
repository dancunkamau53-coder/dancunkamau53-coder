# GitHub Pages Setup Guide

This guide will help you set up your GitHub Pages portfolio.

## Steps to Enable GitHub Pages

### Option 1: Using This Repository

If you want to use this repository (`dancunkamau53-coder`) for GitHub Pages:

1. Go to your repository settings: **Settings → Pages**
2. Under "Build and deployment":
   - Source: Select "Deploy from a branch"
   - Branch: Select "main" and "/(root)"
3. Click "Save"
4. Your site will be published at: `https://dancunkamau53-coder.github.io`

### Option 2: Create a Dedicated Pages Repository (Recommended)

For a proper user page, create a separate repository:

1. Create a new repository named exactly: **`dancunkamau53-coder.github.io`**
2. Clone it locally:
   ```bash
   git clone https://github.com/dancunkamau53-coder/dancunkamau53-coder.github.io.git
   ```
3. Add your portfolio files (index.html, CSS, etc.)
4. Push to GitHub:
   ```bash
   git add .
   git commit -m "Initial portfolio setup"
   git push origin main
   ```
5. Your site will be automatically published at: `https://dancunkamau53-coder.github.io`

## Repository Structure

Your portfolio repository should look like this:

```
dancunkamau53-coder/
├── index.html              # Main portfolio page
├── README.md               # Profile README
├── markdown-practice.md    # Markdown examples
├── .gitignore              # Git ignore file
└── .github/
    └── workflows/          # Optional: CI/CD workflows
```

## Custom Domain (Optional)

To use a custom domain:

1. Purchase a domain from a registrar (Namecheap, GoDaddy, etc.)
2. Go to repository **Settings → Pages**
3. Under "Custom domain", enter your domain name
4. Configure DNS records as per GitHub's instructions

## Troubleshooting

- **Site not showing up?** Wait 1-2 minutes after enabling Pages
- **Wrong domain?** Clear browser cache or try incognito mode
- **404 error?** Ensure `index.html` exists and is in the root directory

For more information, visit: [GitHub Pages Documentation](https://docs.github.com/en/pages)
