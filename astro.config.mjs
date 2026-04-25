// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import icon from 'astro-icon';

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
          label: 'Privacy',
          collapsed: false,
          autogenerate: { directory: 'privacy' },
        },
        {
          label: 'Linux',
          collapsed: false,
          autogenerate: { directory: 'linux' },
        },
        {
          label: 'Visuals',
          collapsed: false,
          autogenerate: { directory: 'visuals' },
        },
      ],
    }),
  ],
});