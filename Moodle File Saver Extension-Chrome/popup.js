
chrome.storage.local.get("latestCourseCode", (data) => {
    document.getElementById("latest-course-code").innerText = data.latestCourseCode || "Not found";
});


chrome.storage.local.get("latestCourseName", (data) => {
    document.getElementById("latest-course-name").innerText = data.latestCourseName || "Not found";
});


