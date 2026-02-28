// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightThemeNova from 'starlight-theme-nova'

// https://astro.build/config
export default defineConfig({

	site: "https://scaredsmods.github.io",
	base: "/docs",
	trailingSlash: "always",

	integrations: [
		starlight({
			plugins: [starlightThemeNova()],
			title: 'ScaredsMods Developer Documentation',
			favicon: './public/favicon.ico',
			logo: {
				light: './src/assets/light-logo.png',
				dark: './src/assets/dark-logo.png'
			},
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/ScaredsMods/docs' }],
			sidebar: [
				{
					label: 'Developer Documentation',
					autogenerate: { directory: 'mods' }
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
			],
			customCss: [
				'./src/styles/custom.css'
			]
		}),
	],
});
