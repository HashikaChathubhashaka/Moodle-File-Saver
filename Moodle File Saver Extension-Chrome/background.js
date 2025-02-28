chrome.downloads.onCreated.addListener((downloadItem) => {
    console.log("Download detected:", downloadItem.filename);


    // Check if the download URL starts with the Moodle URL
    if (downloadItem.url.startsWith("https://online.uom.lk/")) {
        console.log("Download from Moodle:", downloadItem.filename);

    // Get the download item's ID to retrieve the full path later
    const downloadId = downloadItem.id;

    // Wait for the download to finish to get the full path
    chrome.downloads.onChanged.addListener((delta) => {
        if (delta.id === downloadId && delta.state && delta.state.current === "complete") {

            chrome.downloads.search({ id: downloadId }, (results) => {
                if (results && results.length > 0) {
                    const filePath = results[0].filename; 

                    chrome.storage.local.get(["latestCourseName", "latestCourseCode"], (data) => {

                        let latestCourseName = data.latestCourseName || "";
                        let latestCourseCode = data.latestCourseCode || "";

                    fetch("http://localhost:8000/move_files", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            source_file: filePath,
                            destination_folder: `${latestCourseName}-${latestCourseCode}/`

                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log("Python script triggered successfully:", data);
                    })
                    .catch(error => console.error("Error triggering Python script:", error));
                
                });
                
                
                }
            });
        }
    });



    }

    
    else{
        console.log("Download not from Moodle:", downloadItem.filename);
    }


});
