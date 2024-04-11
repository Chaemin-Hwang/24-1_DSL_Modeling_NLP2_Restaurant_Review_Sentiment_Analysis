
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById("triangleChart");
    const ctx = canvas.getContext("2d");

    function drawTriangleChart(ctx, sideLength, taste, service, price) {
        const height = sideLength * (Math.sqrt(3)/2);
        const centerX = 250;
        const centerY = 250;

        [0.8, 0.6, 0.4, 0.2].forEach((scale) => {
            const currentSideLength = sideLength * scale;
            const currentHeight = height * scale;

            ctx.beginPath();
            ctx.moveTo(centerX, centerY - currentHeight / 2);
            ctx.lineTo(centerX - currentSideLength / 2, centerY + currentHeight / 2 * (Math.sqrt(3)/2));
            ctx.lineTo(centerX + currentSideLength / 2, centerY + currentHeight / 2 * (Math.sqrt(3)/2));
            ctx.closePath();
            ctx.strokeStyle = "rgba(0, 0, 0, 0.2)";
            ctx.stroke();
        });

        [1].forEach((scale) => {
            const currentSideLength = sideLength * scale;
            const currentHeight = height * scale;

            ctx.beginPath();
            ctx.moveTo(centerX, centerY - currentHeight / 2);
            ctx.lineTo(centerX - currentSideLength / 2, centerY + currentHeight / 2 * (Math.sqrt(3)/2));
            ctx.lineTo(centerX + currentSideLength / 2, centerY + currentHeight / 2 * (Math.sqrt(3)/2));
            ctx.closePath();
            ctx.strokeStyle = "rgba(0, 0, 0, 1)";
            ctx.stroke();
        });
            // 맛, 서비스, 가격 레이블을 추가
            ctx.font = "15px Arial";
            ctx.fillText(`맛: ${taste}%`, centerX, centerY - height / 2 - 10);
            ctx.fillText(`서비스: ${service}%`, centerX - sideLength / 2 - 30, centerY + height / 2 + 10);
            ctx.fillText(`가격: ${price}%`, centerX + sideLength / 2 -30 , centerY + height / 2 + 10);
            
            // 사용자 데이터 비율에 따라 내부 삼각형을 그림
            // 좌표 계산 로직 수정
            const internalHeight = height * (taste / 100)/ 2;

            const internalSideLength = sideLength * (service / 100)/2;

            const priceAdjustment = price / 100;

            // 맛에 대한 상단 꼭지점
            const tasteX = centerX;
            const tasteY = centerY - internalHeight;

            // 서비스에 대한  꼭지점
            const serviceX = centerX - sideLength* (service / 100)/2 ;
            const serviceY = centerY + sideLength * (service / 100)/2* (Math.sqrt(3)/2)* (Math.sqrt(3)/2) ;

            // 가격에 대한 우측 꼭지점
            const priceX = centerX + (sideLength * (price / 100))/2 ;
            const priceY = centerY + (sideLength * (price / 100))/2 * (Math.sqrt(3)/2)* (Math.sqrt(3)/2) ;

            ctx.beginPath();
            ctx.moveTo(tasteX, tasteY); // 맛
            ctx.lineTo(serviceX, serviceY); // 서비스
            ctx.lineTo(priceX, priceY); // 가격
            ctx.closePath();

            ctx.fillStyle = "rgba(135, 206, 235, 0.5)";
            ctx.fill();
            ctx.strokeStyle = "rgba(135, 206, 235, 1)"; // 테두리 색상을 더 진한 하늘색으로 설정
            ctx.lineWidth = 3;
            ctx.stroke()


        

        

        // Labels and internal triangle drawing code remains the same.
        // Add the rest of your drawTriangleChart function here.
    }

    // Call the drawTriangleChart function with example parameters.
    drawTriangleChart(ctx, 400, 94, 89, 85);
});
