// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import icon from 'astro-icon';

// ─────────────────────────────────────────────────────────────────────────
// If you rename the repo, move the GitHub org, or change the deploy target,
// the same identity is encoded in five places. Update them as a set:
//
//   1. `site`            below — origin used for canonical URLs and sitemap
//   2. `base`            below — URL path prefix (matches the repo name on
//                                 GitHub Pages project sites)
//   3. `social[0].href`  below — "GitHub" icon in the header
//   4. `editLink.baseUrl` below — "Edit page" link shown under each guide
//   5. `src/content/docs/404.md` — two `link:` paths in the hero block
//                                  hard-code `base` because YAML can't run
//                                  expressions; keep them in sync with #2
//
// Other places that reference the repo (README live-site URL, the GitHub
// issue link in 404.md) are not load-bearing and can be updated lazily.
// ─────────────────────────────────────────────────────────────────────────
export default defineConfig({
  site: 'https://chuffed-code.github.io',
  base: '/Chuffed-Guides',
  trailingSlash: 'always',
  integrations: [
    icon(),
    starlight({
      title: 'Chuffed-Guides',                                            
      description: 'Useful guides built with AI.',
      favicon: '/favicon.svg',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/Chuffed-Code/Chuffed-Guides',
        },
      ],
      editLink: {
        baseUrl: 'https://github.com/Chuffed-Code/Chuffed-Guides/edit/main/',
      },
      lastUpdated: true,
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Visuals',
          collapsed: false,
          autogenerate: { directory: 'visuals' },
        },
        {
          label: 'Privacy',
          collapsed: false,
          autogenerate: { directory: 'privacy' },
        },
        {
          label: 'Linux',
          collapsed: false,
          autogenerate: { directory: 'linux' },
        },
      ],
    }),
  ],
});