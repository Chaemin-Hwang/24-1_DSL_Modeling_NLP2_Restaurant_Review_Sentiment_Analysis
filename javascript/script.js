var ctx = document.getElementById('myRadarChart').getContext('2d');
            var myRadarChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['스피드', '파워', '테크닉'],
                    datasets: [{
                        label: '플레이어 스탯',
                        data: [4, 2, 0],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scale: {
                        ticks: {
                            beginAtZero: true,
                            max: 4
                        }
                    }
                }
            });