// File messages.js
document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("messageModal");
    var messageButton = document.getElementsByClassName("message-button");
    var modalHeader = document.getElementById("modal-header");
    var messageContainer = document.getElementById("message-container");
    var messageInput = document.getElementById("message-input");
    var sendButton = document.getElementById("send-button");
    var closeButton = document.getElementsByClassName("close-modal")[0];

    // Fungsi untuk membuka modal
    function openModal(username) {
        modal.style.display = "block";
        modalHeader.textContent = "Send Message to " + username;
    }

    // Fungsi untuk menutup modal
    function closeModal() {
        modal.style.display = "none";
    }

    // Ketika tombol "Message" diklik
    for (var i = 0; i < messageButton.length; i++) {
        messageButton[i].addEventListener("click", function(e) {
            var username = e.target.parentNode.parentNode.querySelector("#other-username").textContent;
            openModal(username);
        });
    }

    // Ketika tombol "Send" di dalam modal diklik
    sendButton.addEventListener("click", function() {
        var messageText = messageInput.value;
        if (messageText.trim() !== "") {
            // Kirim pesan dan tampilkan di dalam modal
            var messageDiv = document.createElement("div");
            messageDiv.textContent = messageText;
            messageContainer.appendChild(messageDiv);
            messageInput.value = "";  // Bersihkan input pesan
        }
    });

    // Ketika tombol "Close" pada modal diklik
    closeButton.addEventListener("click", function() {
        closeModal();
    });

    // Ketika pengguna mengklik di luar modal, tutup modal
    window.addEventListener("click", function(event) {
        if (event.target == modal) {
            closeModal();
        }
    });
});
