---
title: "OSINT Tools for Account Enumeration"
description: "Install and use user-scanner, h8mail, and hashtray to discover every online account linked to your email addresses. Local-first, macOS-focused."
topic: "privacy"
category: "osint"
tags: [osint, account-enumeration, user-scanner, h8mail, hashtray, gravatar]
lastUpdated: 2026-04-23
sidebar:
  order: 10
---

**What this guide covers:** Installing and using the three highest-value open-source tools for discovering every online account linked to your email addresses. All three run locally on your Mac — nothing phones home.

**What you need before starting:** macOS with Terminal access and Python 3.10 or newer installed. If you're not sure whether you have Python, open Terminal and type `python3 --version`. If you get a version number like `Python 3.12.x`, you're good. If you get "command not found," install it from [python.org/downloads](https://python.org/downloads) — download the macOS installer, run it, done.

**Tip:** Each tool installs via `pip`. On macOS, always use `pip3` (not `pip`) to make sure you're installing into Python 3. If you get permission errors, add `--user` to the end of any `pip3 install` command, or use a virtual environment (explained below).

---

## Optional but recommended: use a virtual environment

A virtual environment keeps these tools and their dependencies isolated from the rest of your system. This avoids version conflicts and makes cleanup easy — just delete the folder.

```bash
# Create a folder to hold all your OSINT tools
mkdir ~/osint-tools
cd ~/osint-tools

# Create the virtual environment
python3 -m venv venv

# Activate it (you'll need to do this each time you open a new Terminal session)
source venv/bin/activate

# When active, your prompt will show (venv) at the start
# Now all pip installs go into this environment only

# When you're done working, deactivate with:
deactivate
```

If you use a virtual environment, replace every `pip3 install` below with just `pip install` — inside the venv, `pip` already points to the right Python.

---

## Tool 1: user-scanner — Find which services your email is registered on

**What it does:** Probes the signup, login, and password-reset pages of dozens of services to check whether your email address has an active account. Think of it as the working replacement for Holehe.

**Privacy:** Fully local. It sends HTTP requests directly to each service's public endpoint — no data goes to any third-party API or server.

**GitHub:** [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) (1.2k stars, actively maintained, last release March 2026)

### Install

```bash
# Upgrade pip first (avoids common install issues)
python3 -m pip install --upgrade pip

# Install user-scanner
pip3 install user-scanner
```

That's it. The tool is now available as a command called `user-scanner`.

### Verify it works

```bash
user-scanner --help
```

You should see a help menu listing all available flags. If you get "command not found," try `python3 -m user_scanner --help` instead.

### Basic usage: scan a single email

```bash
user-scanner -e yourname@gmail.com
```

This checks your email against all supported platforms. You'll see color-coded output in your terminal:

- **Registered** = an account exists on that service using your email
- **Not Registered** = no account found
- **Error** = the service blocked the request or timed out (not necessarily a negative — see tips below)

### Scan a specific category only

```bash
# Only check developer platforms (GitHub, GitLab, npm, etc.)
user-scanner -e yourname@gmail.com -c dev

# Only check social platforms
user-scanner -e yourname@gmail.com -c social
```

### List all available modules

```bash
user-scanner -l
```

This shows every platform the tool can check, grouped by category. Useful for understanding what it covers.

### Scan a single specific platform

```bash
user-scanner -e yourname@gmail.com -m github
```

### Scan multiple emails at once (bulk mode)

Create a plain text file with one email per line:

```bash
# Create your email list
nano ~/osint-tools/my-emails.txt
```

Type each email on its own line, then save (Ctrl+O, Enter, Ctrl+X). Then:

```bash
user-scanner -ef ~/osint-tools/my-emails.txt
```

### Save results to a file

```bash
# Save as JSON (best for further processing)
user-scanner -e yourname@gmail.com --json results.json

# Save as CSV (good for spreadsheets)
user-scanner -e yourname@gmail.com --csv results.csv
```

### Show which URLs are being checked (verbose mode)

```bash
user-scanner -v -e yourname@gmail.com
```

This adds the actual URL of each service to the output — helpful for verifying results manually.

### Tips and gotchas

- **Rate limiting:** If you scan too fast or too many emails, some services will temporarily block you. Add a delay between checks with `-d 2` (2-second delay between each platform check).
- **VPN interference:** Some services detect VPN traffic and block it. If you get many errors, try running without your VPN temporarily, or switch to a residential VPN exit.
- **Coverage is still growing.** As of March 2026, user-scanner covers roughly 20–40 platforms (not hundreds). It's the best maintained option, but pair it with h8mail (below) to catch what signup-probing misses.
- **Username scanning too:** user-scanner also checks username availability across platforms. Use `-u yourusername` instead of `-e`. This is useful for finding accounts where you used a consistent username.

---

## Tool 2: h8mail — Find accounts through breach data

**What it does:** Instead of probing login pages, h8mail checks whether your email appears in known data breaches. When a breach entry says "source: LinkedIn 2021," that confirms you had a LinkedIn account — even if LinkedIn has completely patched its signup page against probing. This catches accounts that user-scanner and similar tools will never find.

**Privacy:** The tool itself runs locally. However, to get results, it queries breach databases — some free (like HIBP), some paid (like DeHashed). Those services will see your email address. The `--local` flag lets you search only against local breach files with zero network traffic.

**GitHub:** [khast3x/h8mail](https://github.com/khast3x/h8mail) (4.9k stars, stable)

### Install

```bash
pip3 install h8mail
```

### Verify it works

```bash
h8mail --help
```

### Basic usage: scan without any API keys

```bash
h8mail -t yourname@gmail.com
```

Even without API keys, h8mail will attempt to query free services. Results may be limited, but it's a good starting point to see the tool in action.

### Generate a config file for API keys

This is where h8mail gets powerful. The config file tells h8mail your API keys for various breach lookup services.

```bash
# Generate the template config file in your current directory
h8mail -g
```

This creates a file called `h8mail_config.ini` in your current directory. Open it:

```bash
nano h8mail_config.ini
```

You'll see something like this:

```ini
[h8mail]
;hunterio =
;snusbase_token =
;hibp =
;leak-lookup_pub = 1bf94ff907f68d511de9a610a6ff9263
;leak-lookup_priv =
;emailrep =
;dehashed_email =
;dehashed_key =
;intelx_key =
```

Lines starting with `;` are commented out (inactive). To activate a service, remove the `;` and paste your API key after the `=`.

### Setting up HIBP (Have I Been Pwned) — the most important key

HIBP is the gold standard for breach lookups and the single most valuable API key you can add.

1. Go to [haveibeenpwned.com/API/Key](https://haveibeenpwned.com/API/Key)
2. Purchase an API key (currently $3.50/month — Troy Hunt runs this as a public service, not a business)
3. Copy your key
4. In `h8mail_config.ini`, change the hibp line to:

```ini
hibp = paste-your-key-here
```

Save the file (Ctrl+O, Enter, Ctrl+X).

### Run with your config file

```bash
h8mail -t yourname@gmail.com -c h8mail_config.ini
```

### Scan multiple emails

Create a text file with one email per line (just like for user-scanner):

```bash
h8mail -t ~/osint-tools/my-emails.txt -c h8mail_config.ini
```

### Save results to a file

```bash
# CSV output
h8mail -t yourname@gmail.com -c h8mail_config.ini -o results.csv

# JSON output
h8mail -t yourname@gmail.com -c h8mail_config.ini -j results.json
```

### Hide passwords in output (for demos or screenshots)

```bash
h8mail -t yourname@gmail.com -c h8mail_config.ini --hide
```

This shows only the first 4 characters of any found passwords.

### Understanding the output

h8mail's output is organized per-email. For each email, you'll see entries like:

- **[HIBP]** followed by breach names (e.g., "LinkedIn", "Adobe", "Canva") — each name confirms an account existed at that service
- **Password hashes or cleartext** if found in the breach data — this is why the `--hide` flag exists
- **Related emails** if the breach data links your email to other addresses

**The breach names are your account inventory.** If HIBP says your email appeared in the "Canva 2019" breach, you had a Canva account. Whether it still exists is a separate question, but now you know to check.

### Tips and gotchas

- **HIBP is the priority key.** If you only set up one API key, make it HIBP. It's cheap, privacy-respecting (Troy Hunt is a well-known security researcher), and has the broadest breach coverage.
- **DeHashed** ($5–15/month) provides more detailed records including associated usernames and partial passwords. Useful but not essential for the inventory phase.
- **Local-only mode:** If you have downloaded breach compilations (legal gray area — Bazzell discusses this), you can search them without any network traffic: `h8mail -t yourname@gmail.com -lb /path/to/breach/files/ -sk` (the `-sk` flag skips all API queries).
- **The tool is stable but not actively developed.** It works fine on current Python versions and the API integrations still function. Don't expect new features, but it does its job.

---

## Tool 3: hashtray — Find linked accounts through Gravatar

**What it does:** Gravatar is a service many people unknowingly signed up for (it's bundled with WordPress). If your email has a Gravatar profile, that profile may expose your display name, linked social accounts, verified websites, and bio — all from just an email address. hashtray automates this lookup and can also reverse-search: given a Gravatar username or hash, it attempts to find the associated email.

**Privacy:** Fully local. It queries Gravatar's public API directly — no third party sees your email. The API lookup uses an MD5 hash of your email, which Gravatar already stores.

**GitHub:** [balestek/hashtray](https://github.com/balestek/hashtray) (63 stars, actively maintained, author also contributes to WhatsMyName, Maigret, and Blackbird)

### Install

```bash
pip3 install hashtray
```

### Verify it works

```bash
hashtray --help
```

### Basic usage: check if your email has a Gravatar profile

```bash
hashtray email yourname@gmail.com
```

If a profile exists, hashtray displays:

- **Display name** and bio
- **Linked social accounts** (Twitter/X, GitHub, LinkedIn, etc.)
- **Verified websites and domains**
- **Avatar URL**
- **Whether the email is the primary or secondary email** on the account

If no profile is found, you'll see a message saying no Gravatar profile exists for that hash.

### Why this matters for account inventory

Gravatar profiles often contain links to social accounts and websites that you may have forgotten about. This is data that signup-probing tools like user-scanner cannot find — it comes from what you voluntarily added to your Gravatar profile, possibly years ago.

Additionally, if hashtray says your email is a **secondary** email (not the primary), that means there's another email address associated with the same Gravatar account. You may want to investigate which email that is.

### Reverse lookup: find the email behind a Gravatar username

If you know a Gravatar profile username (the last part of the profile URL, e.g., `gravatar.com/jondoe`):

```bash
hashtray account jondoe
```

Or if you have the MD5 hash (found in avatar URLs like `gravatar.com/avatar/437e4dc6d001f2519bc9e7a6b6412923`):

```bash
hashtray account 437e4dc6d001f2519bc9e7a6b6412923
```

hashtray will attempt to reconstruct the email by generating combinations from the profile's public data (display name, username, etc.) and comparing their MD5 hashes against the account hash.

### Advanced: provide your own hints for reverse lookup

If you have additional info about the account holder, feed it in to improve reverse-lookup accuracy:

```bash
hashtray account jondoe --elements john doe j d jondo 2001
```

This generates more email permutations using the elements you provide.

### Tips and gotchas

- **Most people don't know they have a Gravatar.** If you've ever signed up for WordPress.com, you have one. Many comment systems (Disqus, various WordPress sites) also use Gravatar.
- **Quick check, always worth running.** Even if it returns nothing, the query takes seconds and costs nothing.
- **The data is only as good as what was put in the profile.** If someone never filled out their Gravatar profile, you'll just get the avatar image and a hash.

---

## Putting it all together: your scanning workflow

Now that all three tools are installed, here's the practical workflow for auditing 3–5 email addresses:

### Step 1: Create your target list

```bash
cd ~/osint-tools
nano my-emails.txt
```

Add your emails, one per line:

```
yourname@gmail.com
oldname@yahoo.com
work@company.com
```

### Step 2: Run user-scanner (signup-probing)

```bash
user-scanner -ef my-emails.txt --json user-scanner-results.json -d 2
```

This checks each email against all supported platforms with a 2-second delay between checks. Results saved to JSON.

### Step 3: Run h8mail (breach correlation)

```bash
h8mail -t my-emails.txt -c h8mail_config.ini -o h8mail-results.csv
```

This checks each email against breach databases. The CSV output will list every breach each email appeared in.

### Step 4: Run hashtray (Gravatar pivot)

hashtray doesn't support bulk file input, so run it per-email:

```bash
hashtray email yourname@gmail.com
hashtray email oldname@yahoo.com
hashtray email work@company.com
```

### Step 5: Consolidate your inventory

You now have three complementary data sources:

1. **user-scanner** told you which services currently recognize your email
2. **h8mail** told you which services historically had your email (via breaches)
3. **hashtray** told you what your Gravatar profile exposes (linked accounts, sites, name)

Combine these into a single list of services. That's your account inventory — the starting point for deletion requests.

---

## Quick reference cheat sheet

| Task | Command |
|------|---------|
| **Install user-scanner** | `pip3 install user-scanner` |
| **Install h8mail** | `pip3 install h8mail` |
| **Install hashtray** | `pip3 install hashtray` |
| **Scan one email (user-scanner)** | `user-scanner -e you@email.com` |
| **Scan email file (user-scanner)** | `user-scanner -ef emails.txt --json results.json` |
| **Scan one email (h8mail, no keys)** | `h8mail -t you@email.com` |
| **Scan with HIBP key (h8mail)** | `h8mail -t you@email.com -c h8mail_config.ini` |
| **Generate h8mail config** | `h8mail -g` |
| **Scan email (hashtray)** | `hashtray email you@email.com` |
| **Reverse Gravatar lookup** | `hashtray account username_or_hash` |
| **List user-scanner modules** | `user-scanner -l` |
| **Add delay to user-scanner** | `user-scanner -e you@email.com -d 2` |
| **Hide passwords in h8mail** | `h8mail -t you@email.com --hide` |

---

## Troubleshooting

**"command not found" after install:** Your pip install directory isn't in your PATH. Either use `python3 -m user_scanner` / `python3 -m h8mail` instead, or add `--user` to the install command and restart Terminal.

**Permission errors during install:** Add `--user` to the pip command: `pip3 install user-scanner --user`. Or use a virtual environment (recommended — see top of guide).

**Python version too old:** user-scanner requires Python 3.10+. Check with `python3 --version`. If yours is older, download the latest from python.org.

**Many "Error" results in user-scanner:** Often caused by VPN or ISP blocking. Try without VPN, or use proxy rotation with `-P proxies.txt --validate-proxies`.

**h8mail shows no results without API keys:** Expected. The free tier services it queries are limited. Adding a HIBP key ($3.50/month) dramatically improves results.

**hashtray shows "no profile found":** That email simply doesn't have a Gravatar account. This is a valid negative — move on to the next email.
