<script lang="ts">
	import { AgGridReact } from 'ag-grid-react'; // React Data Grid Component
	import 'ag-grid-community/styles/ag-grid.css'; // Mandatory CSS required by the Data Grid
	import 'ag-grid-community/styles/ag-theme-quartz.css'; // Optional Theme applied to the Data Grid
    import React, { useState } from 'react';

	const [rowData, setRowData] = [
		{ make: 'Tesla', model: 'Model Y', price: 64950, electric: true },
		{ make: 'Ford', model: 'F-Series', price: 33850, electric: false },
		{ make: 'Toyota', model: 'Corolla', price: 29600, electric: false }
	];

	const [colDefs, setColDefs] = [
		{ field: 'make' },
		{ field: 'model' },
		{ field: 'price' },
		{ field: 'electric' }
	];
</script>

<div class="ag-theme-quartz" style="height: 500">
    <react>
	<AgGridReact {rowData} columnDefs={colDefs} />
    </react>
</div>
