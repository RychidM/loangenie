const ctx = document.getElementById("polar-chart").getContext("2d"),
      ctxLine = document.getElementById("line-chart");

const labels = ["January","February","March","April","May","June","July","August","September","October","November","December"];

const dataLine = {
          labels: labels,
          datasets: [{
              label: '',
              data:[114,220,160,150,200,180,180,110,200,180,210,190],
              borderColor: "#246de2",
              pointBackgroundColor: "#fff"
          },
         ],
      };

const data = {
    labels: [
      'Genger',
      'Credit History',
      'Education',
      'Dependants',
      'Marital Status'
    ],
    datasets: [{
      label: 'Eligibility Determinants',
      data: [11, 16, 7, 4, 14],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(75, 192, 192)',
        'rgb(255, 205, 86)',
        'rgb(201, 203, 207)',
        'rgb(54, 162, 235)'
      ] 
    }]
  };

  const config = {
    type: 'polarArea',
    data: data,
    options: {
        responsive:true
    }
  };

  const configLine = {
    type: 'line',
    data: dataLine,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Default Rate'
        }
      }
    },
  };

const myChart = new Chart(ctxLine, configLine);
 
const mypolarChart = new Chart(ctx, config);

