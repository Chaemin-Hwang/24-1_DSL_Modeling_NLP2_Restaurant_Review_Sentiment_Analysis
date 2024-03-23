function showReview(type) {
    // 모든 리뷰를 숨깁니다.
    document.querySelectorAll('.review').forEach(function(review) {
      review.style.display = 'none';
    });
  
    // 선택한 타입의 리뷰만 보여줍니다.
    document.getElementById(type).style.display = 'block';
  }


  