window.onload = function() {
    const reminderMessage = document.getElementById('reminderMessage');
    let flashes = 0;
    const flashInterval = setInterval(function() {
        reminderMessage.style.display = (reminderMessage.style.display === 'none') ? 'block' : 'none';
        flashes++;
        if (flashes >= 10) {  // 5 flashes (block + none = 1 flash)
            clearInterval(flashInterval);
        }
    }, 500);  // Flash every 0.5 seconds
};