<script lang="ts">
	import '../app.css';
	import NavTabs from '$lib/NavTabs.svelte';
	import { AppBar } from '@skeletonlabs/skeleton-svelte';
	import githubIcon from '$lib/assets/github-mark-white.svg?raw';
	import discordIcon from '$lib/assets/discord-logo-white.svg?raw';

	import { page } from '$app/state';

	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();
</script>

<svelte:head>
	<link rel="canonical" href={page.url.href} />
	<meta property="og:url" content={page.url.href} />
	<meta property="og:type" content="website" />
</svelte:head>

<div class="grid h-screen grid-rows-[auto_1fr_auto]">
	<header class="sticky top-0 z-10">
		<AppBar padding="p-1 sm:p-2 md:p-4">
			{#snippet lead()}
				<a href="/" class="md:ml-1">
					<img
						src="/OpenAttribution_logo_wide_200.png"
						alt="Open Attribution"
						class="w-[150px] md:w-[180px]"
					/>
				</a>
			{/snippet}

			<div class="hidden items-center justify-center md:flex">
				<NavTabs />
			</div>

			{#snippet trail()}
				<div class="flex flex-col gap-2 md:gap-4 lg:flex-row">
					<a
						class="btn preset-outlined-primary-900-100 p-2 md:p-4"
						href="https://github.com/OpenAttribution/open-attribution"
						target="_blank"
						rel="noreferrer"
					>
						<div class="flex items-center gap-2">
							<div class="h-4 w-4 md:h-8 md:w-8 md:p-1">
								{@html githubIcon}
							</div>
							<p class="text-center text-sm md:text-base">Star on GitHub</p>
						</div>
					</a>
					<div class="grid grid-cols-2 gap-2 md:gap-4">
						<a
							class="btn preset-outlined-tertiary-500 p-2 md:p-4"
							href="mailto:hello@openattribution.dev"
						>
							<p class="text-center text-sm md:text-base">Email</p>
						</a>

						<a
							class="btn preset-outlined-tertiary-500 p-2 md:p-4"
							href="https://discord.gg/Z5ueYE3Ct3"
							target="_blank"
							rel="noreferrer"
						>
							<div class="gap1 flex items-center justify-center p-1 md:gap-2">
								<span class="flex items-center gap-1">
									<div class="h-4 w-4 md:h-8 md:w-8">
										{@html discordIcon}
									</div>
									<p class="text-center text-sm md:text-base">Discord</p>
								</span>
							</div>
						</a>
					</div>
				</div>
			{/snippet}
		</AppBar>
	</header>

	<main>
		{@render children?.()}
	</main>

	<!--  Mobile only footer -->
	<footer class="bg-surface-50-950 fixed bottom-0 z-10 w-full">
		<AppBar padding="p-0">
			<div class="md:hidden">
				<NavTabs />
			</div></AppBar
		>
	</footer>
</div>
