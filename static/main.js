	
	var myChart;
	var data;
	const onClickHandler = (obj) => {
		$.ajax({
			url: '/data',
			type: 'POST',
			contentType: 'application/json',
			data: JSON.stringify({label: obj.id}),
			success: function (response) {
				myChart.config.data.labels = response.labels
				myChart.config.data.datasets[0].data = response.data
				myChart.config.data.datasets[0].label = response.month
				myChart.update();
			}
		});
	}

	$(function () {
		var $monthChart = $('#one-month-chart');
		$.ajax({
			url: '/data',
			type: 'GET',
			contentType: 'application/json',
			success: function (response) {

				var ctx = $monthChart[0].getContext('2d');
				var data = {
					labels: response.labels,
					datasets: [{
						label: response.month,
						data: response.data,
						backgroundColor: [
							'rgb(255, 99, 132)',
							'rgb(75, 192, 192)',
							'rgb(255, 205, 86)',
							'rgb(54, 162, 235)'
						]
					}]
				};
				var config = {
					type: 'bar',
					data: data,
					options: {
					  scales: {
						y: {
						  beginAtZero: true
						}
					  }
					},
				  };
				myChart = new Chart(
					ctx,
					config
				);
			}
		})
	})