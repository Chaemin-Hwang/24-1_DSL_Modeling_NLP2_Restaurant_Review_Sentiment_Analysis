function handleFiles(files) {
    if (files.length > 0) {
      const file = files[0];
      parseCSV(file);
    }
  }
  
  function parseCSV(file) {
    const reader = new FileReader();
    
    reader.onload = function(event) {
      const csvData = event.target.result;
      Papa.parse(csvData, {
        header: true,
        skipEmptyLines: true,
        complete: function(results) {
          console.log(results);
          displayReviews(results.data);
        }
      });
    };
    
    reader.readAsText(file);
  }
  
  function displayReviews(reviews) {
    const container = document.getElementById('reviews-container');
    container.innerHTML = ''; // Clear previous content
    
    // Create HTML elements for each review and append to the container
    reviews.forEach(review => {
      const reviewDiv = document.createElement('div');
      reviewDiv.className = 'review';
      
      // You may need to change 'reviewer' and 'text' to match the CSV column names
      const reviewerDiv = document.createElement('div');
      reviewerDiv.className = 'reviewer';
      reviewerDiv.textContent = review.reviewer;
      
      const textDiv = document.createElement('div');
      textDiv.className = 'text';
      textDiv.textContent = review.text;
      
      reviewDiv.appendChild(reviewerDiv);
      reviewDiv.appendChild(textDiv);
      
      container.appendChild(reviewDiv);
    });
  }
  