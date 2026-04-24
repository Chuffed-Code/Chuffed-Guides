# Chuffed-Guides

Practical guides made with AI.

**Live site:** <https://chuffed-code.github.io/Chuffed-Guides/>

## What's in here

The site is built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build). Content lives as Markdown under `src/content/docs/`, split into two topic areas today.

### Privacy

A [Bazzell](https://inteltechniques.com)-influenced privacy stack, organized around a master sequencing roadmap at `privacy/index.md` that ties the rest of the guides together in the order they should actually be done.

- **Fundamentals** — a frank ranking of messaging apps, browsers, VPNs, and anonymity tools by threat level, plus a trust-based strategy for keeping your name off property deeds and public records.
- **Identity** — the Proton + SimpleLogin email/alias system with a custom domain, and a Personal Mail Box (PMB) setup that becomes your address of record for banks, bureaus, and data brokers.
- **Browsers** — LibreWolf hardening: `about:config`, uBlock Origin advanced mode, Multi-Account Containers, DNS, and leak verification.
- **Data brokers** — one year of Optery Ultimate to wipe 635+ sites, then zero-cost maintenance via CCPA demand letters.
- **Network** — a pfSense firewall with a VPN kill switch that forces every device in the house through a VPN and drops the internet if it fails.
- **OSINT** — account enumeration with `user-scanner`, `h8mail`, and `hashtray` to find every service linked to an email.
- **Legal — Forced arbitration opt-outs** — overview and universal letter template, plus per-category procedures for finance, streaming, social media, tech/devices, rideshare/delivery, telecom/ISP, and retail/travel.

### Linux

- **Fundamentals** — plain-language guide to Linux terminology, from the kernel up through package managers and desktop environments, anchored to Ubuntu.
- **Desktop environments** — KDE Plasma vs Hyprland on Arch: what each is, the tradeoffs, and how to run both on the same install.

## Run locally

```bash
npm install
npm run dev      # local preview
npm run build    # production build
```

## Structure

Content lives in `src/content/docs/`, organized by topic folder (`privacy/`, `linux/`) and category subfolder. Each guide is a Markdown file with Starlight frontmatter — `title`, `description`, `topic`, `category`, `tags`, `lastUpdated`, and `sidebar.order`. Site configuration (title, sidebar generation, base path, social links, edit-link URL) lives in `astro.config.mjs`.

## License

The entire contents of this repo are dedicated to the public domain under [CC0 1.0 Universal](./LICENSE). You can copy, adapt, translate, or redistribute any of this without permission or attribution.

## Credits

Two tools did the heavy lifting here, and both deserve specific credit:

- **[Claude Opus 4.7](https://www.anthropic.com/claude)** (Anthropic) — content restructuring (turning long, meandering source material into step-by-step guides with consistent structure), sanitization (scrubbing personal details and tightening loose claims), and site planning (the information architecture, the category split, and the sequencing logic that connects the privacy guides into a single roadmap rather than a pile of tips).
- **[Cursor](https://cursor.com)** — the AI-native editor this site was built and is maintained in. The Starlight scaffold, per-guide frontmatter, sidebar wiring, deploy workflow, and this README were all authored inside it.
