<script lang="ts">
	let h1title = 'Own Your MMP Data';
	let h2title = 'Control Your Ad Attribution';

	let title = 'OpenAttribution | Own your MMP data';
	const description =
		'OpenAttribution is an open source mobile attribution platform (MMP) for tracking and analyzing ad campaigns.';
	const keywords =
		'openattribution, open attribution, mmp, mobile, ad tracking, ad analysis, ad platform';
</script>

<svelte:head>
	<title>{title}</title>
	<meta property="og:title" content={title} />
	<meta name="twitter:title" content={title} />
	<meta name="description" content={description} />
	<meta name="keywords" content={keywords} />
	<meta property="og:description" content={description} />
	<meta name="twitter:description" content={description} />
</svelte:head>

<div class="mx-4 md:mx-16 lg:mx-96">
	<div class="card preset-outlined-primary-500 mx-4 mt-8 p-4 text-center">
		<h3 class="h3 text-primary-500">🏗️ Early Alpha: Under Construction 🏗️</h3>
		<p class="">
			This open source project is under construction in the very early alpha stages and is not yet
			ready. If you're interested show some support by starring the project on <a
				href="https://github.com/OpenAttribution/open-attribution"
				target="_blank"
				rel="noreferrer">GitHub</a
			>
			or joining our community on
			<a href="https://discord.gg/Z5ueYE3Ct3" target="_blank" rel="noreferrer">Discord</a>. We also
			welcome any contributors to join in making a new kind of MMP.
		</p>
	</div>

	<div
		class="card preset-filled-surface-100-900 my-12 flex items-center justify-center text-center lg:mt-8"
	>
		<div class="p-2 md:p-4">
			<h1 class="h1 text-center">{h1title}</h1>
			<h2 class="h2 text-primary-500 text-center">{h2title}</h2>
			<h4 class="h4 p-2 text-center lg:p-4">
				Open Attribution is an open source Ad Attribution platform. Fully host your advertising data
				by overseeing its storage, manage your data pipeline and control your advertising campaign
				attribution rules.
			</h4>

			<div class="my-4 flex flex-col items-center justify-center gap-4">
				<a href="/product">
					<button type="button" class="btn preset-outlined-primary-500 justify-center"
						>Learn More</button
					>
				</a>
				<a href="/docs">
					<button type="button" class="btn preset-outlined-tertiary-500">Documentation</button>
				</a>
			</div>
		</div>
	</div>

	<div class="mx-4 grid grid-cols-1 gap-4 md:mx-16 md:mx-8 md:grid-cols-2 lg:mx-32 lg:gap-16">
		<div class="card preset-filled-surface-100-900 p-4">
			<div class="card-header">
				<h3 class="h3 text-primary-900-100">Full Ownership & Privacy</h3>
			</div>
			<div class="card-footer">
				<p>Self-hosted means that your data isn't being mined for value by other companies.</p>
			</div>
		</div>

		<div class="card preset-filled-surface-100-900 p-4">
			<div class="card-header">
				<h3 class="h3 text-primary-900-100">Data Pipeline & Storage</h3>
			</div>
			<div class="card-footer">
				<p>
					Data processing pipelines efficiently store raw data and aggregate for fast analytics and
					dash queries.
				</p>
				<p>Analytics</p>
			</div>
		</div>

		<div class="card preset-filled-surface-100-900 p-4">
			<div class="card-header"><h3 class="h3 text-primary-900-100">Attribution Models</h3></div>
			<div class="card-footer">
				<p>
					You control your attribution models. Last click too old? Try new multi-touch models or
					modern CTV models.
				</p>
			</div>
		</div>

		<div class="card preset-filled-surface-100-900 p-4">
			<div class="card-header">
				<h3 class="h3 text-primary-900-100">Full MMP Analytics Dashboard</h3>
			</div>
			<div class="card-footer">
				<p>
					A full MMP dashboard for your team. User permissions, apps, network settings and ad
					campaign analytics.
				</p>
			</div>
		</div>
	</div>
</div>
