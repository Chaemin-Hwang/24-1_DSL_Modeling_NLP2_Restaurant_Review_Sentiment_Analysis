document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById("triangleChart");
    const ctx = canvas.getContext("2d");

    function drawTriangleChart(ctx, sideLength, taste, service, price) {
        const height = sideLength * (Math.sqrt(3)/2);
        const centerX = 250;
        const centerY = 250;

        // Draw dashed circles as background instead of triangles
        ctx.setLineDash([5, 15]); // Set dash pattern: 5 units on, 15 off
        for (let i = 0; i < 3; i++) {
            ctx.beginPath();
            const radius = sideLength * (i + 1) * 0.2; // 각 원의 반지름 계산
            ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
            ctx.strokeStyle = "rgba(0, 0, 0, 0.2)";
            ctx.stroke();

            // 내부 삼각형 좌표 계산
            const internalTasteX = centerX + Math.cos(Math.PI / 3 * i) * radius * (taste / 100);
            const internalTasteY = centerY - Math.sin(Math.PI / 3 * i) * radius * (taste / 100);
            const internalServiceX = centerX + Math.cos(Math.PI / 3 * (i + 2)) * radius * (service / 100);
            const internalServiceY = centerY - Math.sin(Math.PI / 3 * (i + 2)) * radius * (service / 100);
            const internalPriceX = centerX + Math.cos(Math.PI / 3 * (i + 4)) * radius * (price / 100);
            const internalPriceY = centerY - Math.sin(Math.PI / 3 * (i + 4)) * radius * (price / 100);

            // 내부 삼각형 그리기
            ctx.fillStyle = "rgba(135, 206, 235, 0.5)";
            ctx.beginPath();
            ctx.moveTo(internalTasteX, internalTasteY);
            ctx.lineTo(internalServiceX, internalServiceY);
            ctx.lineTo(internalPriceX, internalPriceY);
            ctx.closePath();
            ctx.fill();
            ctx.strokeStyle = "rgba(135, 206, 235, 1)";
            ctx.lineWidth = 3;
            ctx.stroke();
        }
        ctx.setLineDash([]); // Reset line dash to solid

        // Draw main triangle outline
        ctx.beginPath();
        ctx.moveTo(centerX, centerY - height / 2);
        ctx.lineTo(centerX - sideLength / 2, centerY + height / 2 * (Math.sqrt(3)/2));
        ctx.lineTo(centerX + sideLength / 2, centerY + height / 2 * (Math.sqrt(3)/2));
        ctx.closePath();
        ctx.strokeStyle = "rgba(0, 0, 0, 1)";
        ctx.stroke();

        // Add labels for taste, service, and price
        ctx.fillText(`맛: ${taste}%`, centerX, centerY - height / 2 - 10);
        ctx.fillText(`서비스: ${service}%`, centerX - sideLength / 2 - 30, centerY + height / 2 + 20);
        ctx.fillText(`가격: ${price}%`, centerX + sideLength / 2 , centerY + height / 2 + 20);
    }

    // Call the drawTriangleChart function with example parameters
    drawTriangleChart(ctx, 400, 40, 60, 40);
});
