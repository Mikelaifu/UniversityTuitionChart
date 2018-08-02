
var $buttonname = Plotly.d3.select("#buttonname"); 


function BuildDropdown() {
  // Get data from '/names' endpoint
  
  url = "/dropdown"
  Plotly.d3.json(url, function(error, response) {
      console.log(response)
      $buttonname.on('change', optionChanged);

      // Add options to dropdown
      var options = $buttonname 
          .selectAll('option')
          .data(response).enter()
          .append('option')
              .text(d => d);
      
      // Add a blank option at the top.
      var $ddBlank = $buttonname.insert("option", ":first-child")
          .text("Select School...").attr("value", "").attr("selected", true);
      });
}

function optionChanged() {
  
selectedCollege = Plotly.d3.select('#buttonname').property('value');

updateLineChart(selectedCollege);


};


BuildDropdown();






// function buildLineChart(Percentile, ID, CollegeName= "") {

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
    };   
        
function updateLineChart(collegename) {
    
        // Get data from '/sample/<sample>' endpoint (for our metadata table)
    url = '/line'
    Plotly.d3.json(url, function(error, response) {
        console.log(response.college[collegename]);
        
        var newcolor = getRandomColor()

        var trace1 = {x: response.college.Year,
            y: response.college[collegename], 
            line: {color: newcolor},
           name: collegename};
    
            
            Plotly.addTraces("1", trace1);

            Plotly.addTraces("2", trace1);

            Plotly.addTraces("3", trace1);
            Plotly.addTraces("4", trace1);

            Plotly.addTraces("5", trace1);
            
            Plotly.addTraces("6", trace1);


    
        });
    };
        

function buildLineChart(Percentile, ID) {

    // Get data from '/sample/<sample>' endpoint (for our metadata table)
    url = '/line'
    Plotly.d3.json(url, function(error, response) {
        console.log(response.standerd[Percentile]);
        

        var trace = {
           type: "scatter",
           mode: "lines",
           x: response.college.Year,
           y: response.standerd[Percentile],
           line: {color: '#17BECF'}

       }

       global_trace = trace;

       var data = [trace];

       

    var layout = {
            autosize: false,
            width: 500,
            height: 450,
            margin: {
              l: 25,
              r: 25,
              b: 25,
              t: 25,
            //   pad: 3
            },
            showlegend: true,
            legend: {
                x: 0,
                y: 1
              },
            
             yaxis: {
               title: "amount"
             },
             xaxis: {
               title: "Year"
             },
            
            plot_bgcolor: '#A0F7E6',
            
          };
       
       Plotly.newPlot(ID, data, layout);

   

        })
        
    };



    buildLineChart('Percentile0_40', "1");
    buildLineChart('Percentile40_60', "2");
    buildLineChart('Percentile60_75', "3");
    buildLineChart('Percentile75_86', "4");
    buildLineChart('Percentile86_95', "5");
    buildLineChart('Percentile95_100', "6");

    


    
    
      