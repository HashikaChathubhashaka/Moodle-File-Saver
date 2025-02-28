// Get the page title
let title = document.title;
let Coursepage = title.split(":")
let CourseExist = Coursepage[0] == "Course" ? true : false
// Match the text between ':' and '|'
let match = title.match(/:\s*(.*?)\s*\|/);
let fullCourseText = match ? match[1].trim() : "Course Not Found";

// Split by ' - ' to extract parts
let parts = fullCourseText.split(" - ");

let moduleParts = parts[0].split("-");
let moduleNumber = moduleParts.length > 2 && CourseExist ? moduleParts[2].trim() : "Module code Not Found";
let courseName = parts.length > 1 && CourseExist ? parts.slice(1).join(" - ").trim() : "Course Name Not Found";

// Retrieve the previous latest course name and code
chrome.storage.local.get(["latestCourseName", "latestCourseCode"], (data)  => {
    const previousCourseName = data.latestCourseName || "";
    const previousCourseCode = data.latestCourseCode || "";

    // Determine the new latest course name and code
    const newLatestCourseName = courseName !== "Course Name Not Found" ? courseName : previousCourseName;
    const newLatestCourseCode = moduleNumber !== "Module code Not Found" ? moduleNumber : previousCourseCode;

    // Store the values in Chrome storage
    chrome.storage.local.set({ 
        moduleNumber: moduleNumber, 
        courseName: courseName,
        latestCourseCode: newLatestCourseCode,
        latestCourseName: newLatestCourseName 
    }, () => {
        console.log("Extracted Module Number:", moduleNumber);
        console.log("Extracted Course Name:", courseName);
        console.log("latest Course code:", newLatestCourseCode);
        console.log("Latest Course Name:", newLatestCourseName); // this is what we need 
    });
});
