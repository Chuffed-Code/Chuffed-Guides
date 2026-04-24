---
title: "LibreWolf Hardening Guide"
description: "Step-by-step hardening of LibreWolf beyond its already strong defaults. Covers about:config tweaks, uBlock Origin advanced mode, containers, and verification."
topic: "privacy"
category: "browsers"
tags: [librewolf, firefox, browser-hardening, ublock-origin, containers, bazzell, arkenfox]
lastUpdated: 2026-04-23
sidebar:
  order: 10
---

A step-by-step guide to hardening LibreWolf beyond its already strong defaults. Based on methodologies from Bazzell, Arkenfox, and community best practices.

**Zero Telemetry · Anti-Fingerprinting · Container Isolation**

## Phase 0 — What LibreWolf already handles

These are things Bazzell recommends for Firefox that LibreWolf does out of the box. No action needed.

- Telemetry, crash reports, normandy, studies, and personalized recommendations are completely disabled at compile time.
- Pocket extension is removed at compile time — not just disabled.
- Mozilla VPN ads and Firefox account prompts are removed.
- uBlock Origin is pre-installed with default filter lists active.
- Default search engine is DuckDuckGo with no search suggestions.
- HTTPS-Only Mode is enabled in all windows.
- Cookies and site data are deleted when the browser closes.
- Tracking protection is set to Strict by default.
- Resist Fingerprinting (RFP) is enabled — same tech used by Tor/Mullvad Browser.
- New tabs and homepage default to blank pages.
- Firefox Sync is disabled unless you explicitly enable it.
- dFPI (dynamic First Party Isolation) handles cross-site cookie isolation automatically.

This means about 70–80% of what Bazzell's Firefox hardening guide covers is already done for you. The steps below focus on what's *left* to configure.

## Phase 1 — LibreWolf Settings Menu

Open the menu → Settings. Verify and adjust these options.

### 🔒 Privacy & Security

Most privacy settings are pre-configured, but verify the following:

- Under **Permissions**, click "Settings" next to Location, Camera, Microphone, Notifications, and Virtual Reality. Check **"Block new requests"** on each.
- Under **Deceptive Content and Dangerous Software Protection** — uncheck all options. This prevents sharing site visit data with Google's Safe Browsing service. (LibreWolf may already disable this, but verify.)
- Ensure **"Delete cookies and site data when Firefox is closed"** is checked. If you need persistent logins for containers, you'll add exceptions later.
- Confirm History is set to **"Use custom settings"** with "Remember browsing and download history" and "Remember search and form history" both **unchecked**.
- Confirm **"Clear history when Firefox closes"** is checked. Do NOT check "Always use private browsing mode" — this breaks Containers.

### 🔍 Search

Verify these are properly set:

- Default search engine should be **DuckDuckGo** (or consider switching to **SearXNG** or **StartPage** for better results).
- All options under **"Provide search suggestions"** should be unchecked.

### 📋 General

- Uncheck **"Recommend extensions as you browse"** and **"Recommend features as you browse"** if not already disabled.

### 🔗 LibreWolf Advanced Settings

LibreWolf has its own settings panel. Access it via the puzzle-piece icon or `about:preferences` and look for the LibreWolf-specific section. Here you can:

- Enable **automatic add-on updates** — LibreWolf disables this by default but it's safe to turn on for convenience.
- Optionally enable **Firefox Sync** if you need cross-device bookmarks (understand the privacy tradeoff).

## Phase 2 — about:config Tweaks

Type `about:config` in the URL bar. Search for each setting and adjust. LibreWolf already sets many of these — only change what isn't already correct.

:::caution
Check each value before changing. LibreWolf likely has many of these pre-configured. Only modify settings that differ from the recommended value.
:::

### Geolocation & Fingerprinting

| Setting | Value | Purpose |
|---|---|---|
| `geo.enabled` | `false` | Disables browser location sharing |
| `dom.battery.enabled` | `false` | Blocks battery level fingerprinting |
| `webgl.disabled` | `true` | Prevents WebGL-based fingerprinting. May break some 3D sites. |
| `media.navigator.enabled` | `false` | Hides media device enumeration |
| `dom.webnotifications.enabled` | `false` | Disables embedded web notifications |

### Network & Prefetching

| Setting | Value | Purpose |
|---|---|---|
| `network.http.sendRefererHeader` | `0` | Stops sites from seeing where you came from. May break some logins. |
| `network.dns.disablePrefetch` | `true` | Prevents speculative DNS lookups |
| `network.dns.disablePrefetchFromHTTPS` | `true` | Same for HTTPS pages |
| `network.prefetch-next` | `false` | Stops preloading linked pages |

### WebRTC Leak Prevention

:::caution
These settings prevent IP leaks through WebRTC. If you use browser-based video conferencing (Zoom in browser, Google Meet, etc.), skip these — they will break those services.
:::

| Setting | Value | Purpose |
|---|---|---|
| `media.peerconnection.enabled` | `false` | Disables WebRTC entirely |
| `media.peerconnection.turn.disable` | `true` | Disables TURN relay |
| `media.peerconnection.use_document_iceservers` | `false` | Prevents ICE server usage |
| `media.peerconnection.video.enabled` | `false` | Blocks WebRTC video |

### PDF & Misc Security

| Setting | Value | Purpose |
|---|---|---|
| `pdfjs.enableScripting` | `false` | Prevents malicious JavaScript in PDFs |
| `media.autoplay.default` | `5` | Blocks all audio and video autoplay |
| `browser.safebrowsing.malware.enabled` | `false` | Disables Google's malware check (sends data to Google) |
| `identity.fxaccounts.enabled` | `false` | Disables Firefox account integration |

## Phase 3 — Harden uBlock Origin

LibreWolf ships with uBlock Origin, but default settings can be tightened.

### ⚙️ Enable Advanced Mode

Click the uBlock Origin icon → Dashboard (gear icon) → Settings tab.

- Check **"I am an advanced user"**. This unlocks per-site script control in the popup.

### 📋 Enable Additional Filter Lists

Go to the **Filter lists** tab. Enable these additional lists:

- Under **Privacy**: Enable **"Block Outsider Intrusion into LAN"** — protects local network devices.
- Under **Privacy**: Enable **"AdGuard URL Tracking Protection"** — strips tracking parameters from URLs.
- Under **Annoyances**: Enable **"EasyList/uBO – Cookie Notices"** — blocks GDPR/cookie popups.

Click **"Apply changes"** then **"Update now"**.

### 🛡️ Using the Advanced Popup

With advanced mode on, the uBlock popup now shows a grid of scripts per site. Key techniques from Bazzell:

- **Default browsing:** Leave everything alone. uBlock handles blocking automatically.
- **Visiting a suspicious site:** Click the far-right (red) of the top cell in the 2nd column to block ALL scripts globally. Reverse when done.
- **Bypassing paywalls:** Try blocking **"3rd-party scripts"** in the 3rd column (site-specific). Save and reload.
- **Resetting if you break things:** Go to Dashboard → My Rules → delete all Temporary Rules → Save → Commit.

## Phase 4 — Recommended Extensions

Keep extensions minimal — each one increases your attack surface and fingerprint uniqueness.

:::tip
LibreWolf's own documentation recommends keeping a very minimal addon setup. Only install what you actually need.
:::

**uBlock Origin** *(Pre-installed)*
: Ad/tracker/script blocker. Already included — just configure the advanced settings from Phase 3.

**Multi-Account Containers** *(Essential for Aliases)*
: Isolate sessions within tabs. Required for managing multiple accounts on the same service simultaneously. See Phase 5.

**KeePassXC-Browser or Bitwarden** *(Recommended)*
: Password manager integration. Note: KeePassXC requires native messaging setup on Linux/Mac — check LibreWolf FAQ for instructions.

**CanvasBlocker** *(Optional)*
: Additional fingerprinting protection on top of RFP. Spoofs canvas, audio, and WebGL data. Useful if you disabled RFP for compatibility.

**Skip Redirect** *(Optional)*
: Bypasses tracking redirects and goes directly to the destination URL. Reduces tracking data leakage.

**User-Agent Switcher** *(Optional)*
: Emulate different browsers/devices. Useful for OSINT or accessing mobile-only content. Use sparingly — can make you more unique.

:::caution
Avoid installing Privacy Badger, Disconnect, or Adblock Plus alongside uBlock Origin — they are redundant and add fingerprint surface. uBlock Origin replaces all of them.
:::

## Phase 5 — Container Setup (Bazzell Method)

Replicate Bazzell's container workflow for identity isolation within LibreWolf.

:::tip
LibreWolf's dFPI already isolates cookies between sites. Containers add the ability to maintain **multiple simultaneous logins** on the same service and create **dedicated isolation zones**.
:::

### 📦 Install & Configure

- Install **Multi-Account Containers** from Firefox Add-ons.
- Pin the icon to your toolbar: Extensions menu → right-click → "Pin to Toolbar".
- Open the Containers menu → **Manage Containers**.
- **Delete all default containers** (Personal, Work, Banking, Shopping).
- Create new containers: **Alias 01**, **Alias 02**, **Alias 03**, **Alias 04** (minimum). Assign unique colors and icons to each.

### 🔄 Usage Patterns

**👤 Multiple Logins**
: Open Facebook in Alias 01, log into Account A. Open Containers menu → Alias 02 → Facebook → log into Account B. Switch between tabs freely.

**🛡️ Safe Link Opening**
: Right-click any suspicious link → "Open Link in New Container" → select a different alias. The destination can't see cookies from your current session.

**📌 Dedicated Containers**
: Assign Google to always open in a "Google" container. All Google traffic is isolated regardless of which tab you clicked from.

**🔒 Limit Sites**
: In Manage Containers, enable "Limit to Designated Sites" for sensitive containers. Prevents accidental navigation to unintended sites.

### 📌 Setting Up Dedicated Site Containers

To force a site to always open in a specific container (e.g., isolate all Google traffic):

- Create a container called **"Google"**.
- Open a new tab in the Google container.
- Navigate to **google.com**.
- Click the Containers menu → **"Always open this site in…"** → select the Google container.
- Navigate to google.com from a normal tab → select **"Remember my decision"** → click "Open in Google".
- This now applies to all Google services (Gmail, Google Voice, etc.).

:::tip
If you need persistent logins inside containers (e.g., staying logged into a service across browser restarts), you'll need to add cookie exceptions for those specific domains in Privacy & Security → Manage Exceptions.
:::

## Phase 6 — DNS & Verification

Configure encrypted DNS and verify your hardening is working.

### 🌐 Browser-Level DNS over HTTPS

This ensures your DNS queries are encrypted and not visible to your ISP, even on public Wi-Fi.

- Open `Settings → Network Settings → Settings`.
- Scroll to **"Enable DNS over HTTPS"**.
- Select **"Max Protection"** and choose a provider:
  - **NextDNS** — custom filtering + analytics. Use your custom URL: `https://dns.nextdns.io/YOUR_ID`
  - **Quad9** — malware blocking, no logging.
  - **Mullvad DNS** — no logging, ad blocking option.
- For NextDNS with forced mode: go to `about:config` → set `network.trr.mode` to `3` (DNS over HTTPS only, no fallback).

### ✅ Verify Your Configuration

Test your hardened setup with these tools:

- [browserleaks.com/webrtc](https://browserleaks.com/webrtc) — Goal: all red "False" responses (no IP leaks)
- [browserleaks.com/geo](https://browserleaks.com/geo) — Goal: red "Denied" result
- [browserleaks.com/proxy](https://browserleaks.com/proxy) — Goal: all red "not detected" results
- [browserleaks.com/social](https://browserleaks.com/social) — Goal: no logged-in sessions detected (test container isolation)
- [browserleaks.com/javascript](https://browserleaks.com/javascript) — Review: check browser identifiers and OS data
- [coveryourtracks.eff.org](https://coveryourtracks.eff.org) — EFF's fingerprint uniqueness test
- [privacytests.org](https://privacytests.org) — Automated cross-browser privacy comparison
- [cloudflare.com/ssl/encrypted-sni](https://cloudflare.com/ssl/encrypted-sni) — Goal: green checks on DNSSEC and TLS

### 🏗️ Recommended Browser Stack

For comprehensive coverage, consider using multiple browsers for different purposes:

**🦁 Brave** — *Daily driver.* Fast, Chromium-compatible, good privacy defaults. Use for casual browsing and sites that break on hardened browsers.

**🐺 LibreWolf (Hardened)** — *Primary secure browser.* Containers for identity management, persistent sessions, research, and sensitive accounts.

**🔒 Mullvad Browser** — *Maximum anonymity.* Use for sensitive lookups where you need zero fingerprint. Pair with Mullvad VPN. No persistent state.

---

*Sources: Michael Bazzell (Extreme Privacy & OSINT Techniques) · LibreWolf Documentation · Privacy Guides · PrivacyTests.org*

*Guide compiled March 2026 · Review and update periodically as browser versions change*
