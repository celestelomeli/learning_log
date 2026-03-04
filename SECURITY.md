# Security Notes

## SECRET_KEY Rotation

**Date:** March 3, 2026  
**Action:** Rotated Django SECRET_KEY

### Background
The original SECRET_KEY was hardcoded in `settings.py` and committed to Git history. This key is now considered compromised and has been rotated.

### What Was Done
1. Generated a new SECRET_KEY using Django's `get_random_secret_key()` utility
2. Moved SECRET_KEY to environment variables (`.env` file)
3. Updated `settings.py` to read SECRET_KEY from environment
4. Added `.env` to `.gitignore` to prevent future commits

### Important
**DO NOT reuse the old SECRET_KEY** (`django-insecure-xa$j-a+m%r@-x(kvs*rtgs_7qq8ofdhpsqe5+rv-2wd=8lai-t`).

This key was exposed in Git history and should be considered public. Any production deployments must use a new, securely generated key.

### Generating a New SECRET_KEY
To generate a new SECRET_KEY for production:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Store the generated key in your production environment's secrets manager (AWS Secrets Manager, environment variables, etc.).

## Security Best Practices

### Environment Variables
- Never commit `.env` files to version control
- Use different SECRET_KEYs for development, staging, and production
- Rotate secrets regularly (at least annually, or immediately if compromised)

### Production Deployment
- Always set `DEBUG=False` in production
- Use HTTPS (enforced via `SECURE_SSL_REDIRECT=True`)
- Configure `ALLOWED_HOSTS` to only include your actual domains
- Use a secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.)

### Reporting Security Issues
If you discover a security vulnerability, please email [your-email@example.com] instead of opening a public issue.
