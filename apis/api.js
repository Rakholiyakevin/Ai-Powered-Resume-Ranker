document.getElementById('submitButton').addEventListener('click', sendResumeData);

async function sendResumeData() {
    const path = "./pdfs";  // You can collect this input dynamically from user
    const user_skills = ['html', 'css', 'ruby', 'java'];  // Skills array from user input
    const degree = "computer Science";  // Degree input from user

    try {
        const response = await fetch('http://127.0.0.1:5000/process-resume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                path: path,
                user_skills: user_skills,
                degree: degree
            })
        });

        const data = await response.json();
        
        if (response.ok) {
            console.log("Success:", data);
            // You can display or handle the result on the front-end as needed
        } else {
            console.error("Error:", data);
        }
    } catch (error) {
        console.error("Request failed:", error);
    }
}
