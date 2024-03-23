document.getElementById('view-all-reviews').addEventListener('click', function() {
    window.location.href = 'review_moa.html';
  });

function toggleReview(reviewId) {
    var content = document.getElementById(reviewId);
    if (content.style.display === 'none') {
      content.style.display = 'block';
    } else {
      content.style.display = 'none';
    }
  }