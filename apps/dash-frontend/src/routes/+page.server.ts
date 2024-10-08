import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ parent, url }) => {
	// depends(`page:${url.searchParams}`);
	const startDate = url.searchParams.get('start');
	const endDate = url.searchParams.get('end');
	const { respApps, respNets } = await parent();

	return {
		respData: fetch(
			`http://dash-backend:8001/api/overview?start_date=${startDate}&end_date=${endDate}`
		)
			.then((resp) => {
				if (resp.status === 200) {
					return resp.json();
				} else if (resp.status === 404) {
					console.log('Not found');
					return 'Not Found';
				} else if (resp.status === 500) {
					console.log('API Server error');
					return 'Backend Error';
				}
			})
			.then(
				(json) => json,
				(error) => {
					console.log('Uncaught error', error);
					return 'Uncaught Error';
				}
			),
		respNets,
		respApps
	};
};
