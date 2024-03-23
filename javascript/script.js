// 카테고리 버튼 요소들을 가져옵니다.
const positiveButton = document.getElementById('positiveButton');
const negativeButton = document.getElementById('negativeButton');

// 리뷰 텍스트를 가져옵니다.
const reviewText = document.getElementById('reviewText');

// 긍정 카테고리 버튼을 클릭했을 때의 이벤트 리스너
positiveButton.addEventListener('click', function() {
    // 부정 카테고리 버튼에서 selected 클래스를 제거합니다.
    negativeButton.classList.remove('selected');
    // 긍정 카테고리 버튼에 selected 클래스를 추가합니다.
    positiveButton.classList.add('selected');
    // 리뷰 텍스트 내용을 변경합니다.
    reviewText.textContent = "이 제품은 정말 좋습니다!";
});

// 부정 카테고리 버튼을 클릭했을 때의 이벤트 리스너
negativeButton.addEventListener('click', function() {
    // 긍정 카테고리 버튼에서 selected 클래스를 제거합니다.
    positiveButton.classList.remove('selected');
    // 부정 카테고리 버튼에 selected 클래스를 추가합니다.
    negativeButton.classList.add('selected');
    // 리뷰 텍스트 내용을 변경합니다.
    reviewText.textContent = "이 제품은 기대에 못 미칩니다.";
});