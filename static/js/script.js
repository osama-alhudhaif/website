// تحديث السنة تلقائياً
document.addEventListener("DOMContentLoaded", function () {
    const yearEl = document.getElementById("year");
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // إظهار وإخفاء التصنيفات
    const showCategoriesBtn = document.getElementById("show-categories");
    const categoryBox = document.getElementById("category-box");
    if (showCategoriesBtn && categoryBox) {
        showCategoriesBtn.addEventListener("click", function () {
            categoryBox.style.display =
                categoryBox.style.display === "none" ? "block" : "none";
        });
    }

    // وظيفة زر الإشعارات - فقط إذا كان موجود (يعني المستخدم مسجل دخول)
    const notificationsBtn = document.getElementById("notifications-btn");
    const notificationDropdown = document.getElementById("notification-dropdown");

    if (notificationsBtn && notificationDropdown) {
        notificationsBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            notificationDropdown.style.display =
                notificationDropdown.style.display === "none" ? "block" : "none";
        });

        // إغلاق القائمة عند الضغط خارجها
        document.addEventListener("click", function (event) {
            if (
                !notificationsBtn.contains(event.target) &&
                !notificationDropdown.contains(event.target)
            ) {
                notificationDropdown.style.display = "none";
            }
        });

        // منع الإغلاق عند الضغط على القائمة نفسها
        notificationDropdown.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }

    // تأثيرات التحميل
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 0.3s ease-in-out";

    setTimeout(function () {
        document.body.style.opacity = "1";
    }, 100);
});
