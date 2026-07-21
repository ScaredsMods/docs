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
			favicon: './favicon.svg',
			logo: {
				light: './src/assets/light-logo.png',
				dark: './src/assets/dark-logo.png'
			},
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/ScaredsMods/docs' }],
			sidebar: [
				{
  					label: 'Mods',
  					items: [
						'mods',
  					    { label: 'MoreOutputsAPI', autogenerate: { directory: 'mods/moapi' } },
  					],
				},
				{
  					label: 'Plugins',
  					items: [
					   'plugins',
  					   { label: 'SubCommandLib', autogenerate: { directory: 'plugins/scl' } },
  					],
				},
				{
  					label: 'Reference',
  					items: [
						{ label: 'Mods', autogenerate: { directory: 'reference/mods' } },
  					    { label: 'Plugins', autogenerate: { directory: 'reference/plugins' } },
  					],
				},
			],
			customCss: [
				'./src/styles/custom.css'
			]
		}),
	],
});
