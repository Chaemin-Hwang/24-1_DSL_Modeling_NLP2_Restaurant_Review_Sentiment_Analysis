document.getElementById('view-all-reviews').addEventListener('click', function() {
    window.location.href = 'review_moa.html';
  });

  function showReview(type) {
    // 모든 리뷰를 숨기고 모든 버튼에서 'selected' 클래스를 제거합니다.
    var reviews = document.getElementsByClassName('review');
    for (var i = 0; i < reviews.length; i++) {
        reviews[i].style.display = 'none';
    }

    // 해당 타입의 리뷰를 표시합니다.
    document.getElementById(type).style.display = 'block';

    // 모든 리뷰 버튼에서 'selected' 클래스를 제거합니다.
    var buttons = document.querySelectorAll('#reviewButtons button, #reviewbuttons button');
    buttons.forEach(function(button) {
        button.parentElement.classList.remove('selected');
    });

    // 클릭된 버튼에 'selected' 클래스를 추가합니다.
    var selectedButton = document.querySelector(`button[onclick="showReview('${type}')"]`);
    if (selectedButton) {
        selectedButton.parentElement.classList.add('selected');
    }

    // 선택된 버튼에 따라 슬라이더 위치를 조정합니다.
    updateSlider(type);
}

function updateSlider(type) {
    // 'selected' 위치 슬라이더 업데이트를 위한 클래스를 추가합니다.
    var selectBox = document.querySelector('.select_box');
    if (type === 'positive') {
        selectBox.classList.add('positive-selected');
        selectBox.classList.remove('negative-selected');
    } else {
        selectBox.classList.add('negative-selected');
        selectBox.classList.remove('positive-selected');
    }
}


