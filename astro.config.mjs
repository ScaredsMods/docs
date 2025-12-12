// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({

	site: "https://scaredsmods.github.io",
	base: "/docs",
	trailingSlash: "always",

	integrations: [
		starlight({
			title: 'ScaredsMods | Documentation ',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/ScaredsMods/docs' }],
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
			],
		}),
	],
});
