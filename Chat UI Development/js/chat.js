$(document).ready(function () {
    // UI Elements
    const $messageInput = $('#messageInput');
    const $sendBtn = $('#sendBtn');
    const $messagesContainer = $('#messagesContainer');
    const $welcomeScreen = $('#welcomeScreen');
    const $typingIndicator = $('#typingIndicator');
    const $chatArea = $('#chatArea');
    const $sidebar = $('#sidebar');
    const $sidebarOverlay = $('#sidebarOverlay');

    // Audio elements (Bonus)
    const sendSound = document.getElementById('sendSound');
    const receiveSound = document.getElementById('receiveSound');

    // State
    let isFirstMessage = true;
    let isWaitingForResponse = false;

    function getMockResponse(userInput) {
        const text = userInput.toLowerCase();

        // ---------------------------------------------------------
        // Exact Matches for Sidebar & Suggestion Cards
        // ---------------------------------------------------------
        
        // Match: "CSS Flexbox Layout Tricks"
        if (text.includes('flexbox layout tricks')) {
            return "Here are three powerful **CSS Flexbox layout tricks** that will save you time:\n\n### 1. The Holy Grail of Centering\nPerfectly center vertical and horizontal content with just three lines applied to a container:\n```css\n.parent {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n```\n\n### 2. Auto Margins for Pushing Elements\nIf you have a navbar and want the 'Login' button pushed explicitly to the far right, apply `margin-left: auto;` to that specific button. Flexbox will automatically push it to the edge!\n\n### 3. Equal Height Columns\nUnlike `float` layouts, Flexbox children automatically stretch to the height of the tallest sibling by default, since `align-items: stretch` is the default property behavior.\n\nExperiment with these on your next layout!";
        } 
        
        // Match: "JavaScript Promises Guide"
        else if (text.includes('promises guide') || text.includes('javascript promises guide')) {
            return "### The Ultimate Guide to JavaScript Promises\n\nA Promise handles asynchronous operations smoothly, preventing deeply nested 'callback hell'.\n\n**1. Consuming a Promise (.then / .catch):**\nWhen you call `fetch()`, it returns a promise.\n```javascript\nfetch('https://api.example.com/data')\n  .then(response => response.json())\n  .then(data => console.log(data))\n  .catch(error => console.error(\"Request failed:\", error));\n```\n\n**2. The Modern Approach (`async / await`):**\nInstead of `.then()`, you can pause execution until the promise resolves. This looks like synchronous code!\n```javascript\nasync function loadData() {\n  try {\n    const response = await fetch('https://api.example.com/data');\n    const data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error(\"Request failed:\", error);\n  }\n}\n```\nPromises are essential for any API integration!";
        } 
        
        // Match: "Bootstrap 5 Grid System"
        else if (text.includes('bootstrap 5 grid system')) {
            return "Bootstrap 5 uses a highly responsive, mobile-first flexbox grid system built on a **12-column layout**.\n\n### Core Rules:\n1. **Rows must be in a container:** Use `.container` (fixed-width) or `.container-fluid` (100% width).\n2. **Rows are wrappers for columns:** Only `.col` classes should be immediate children of `.row`.\n3. **Columns sum up to 12:** If you place `.col-4` and `.col-8` in a row, they take up the full 12-column width.\n\n### Example Responsive Layout:\n```html\n<div class=\"container\">\n  <div class=\"row\">\n    <!-- Takes up 12 cols on mobile, but 6 cols (half width) on medium screens -->\n    <div class=\"col-12 col-md-6\">Left Panel</div>\n    <div class=\"col-12 col-md-6\">Right Panel</div>\n  </div>\n</div>\n```\nBootstrap breakpoints are `sm`, `md`, `lg`, `xl`, and `xxl`. Enjoy building!";
        } 
        
        // Match: "Help me write a Python script for automation"
        else if (text.includes('automation') && (text.includes('python') || text.includes('script'))) {
            return "Certainly! Here is a powerful Python automation script that automatically organizes files in a messy downloads folder by moving them into categorized sub-folders based on their extensions (e.g., `.pdf` goes to `PDF_Files`).\n\n```python\nimport os\nimport shutil\n\ndef organize_folder(folder_path):\n    # Iterate through all files in the directory\n    for filename in os.listdir(folder_path):\n        file_path = os.path.join(folder_path, filename)\n        \n        # Skip directories, handle only files\n        if os.path.isdir(file_path): continue\n            \n        # Extract extension\n        ext = filename.split('.')[-1].upper()\n        target_dir = os.path.join(folder_path, f'{ext}_Files')\n        \n        # Create the directory if it doesn't exist\n        if not os.path.exists(target_dir):\n            os.makedirs(target_dir)\n            \n        # Move the file\n        shutil.move(file_path, os.path.join(target_dir, filename))\n    print(\"Folder organization complete!\")\n\n# Run the automation\norganize_folder('/path/to/downloads')\n```\n\nBefore running this, make sure to change `/path/to/downloads` to a safe test directory!";
        } 
        
        // Match: "Summarize the main points of CSS Grid"
        else if (text.includes('summarize') && text.includes('grid')) {
            return "Here is a concise summary of the core capabilities of **CSS Grid**:\n\n- **Two-Dimensional Layouts:** Unlike Flexbox (which is primarily 1D), CSS Grid is designed to handle both columns and rows simultaneously.\n- **Direct Parent/Child Control:** Applied structure via `display: grid;` to a container, customizing it globally using `grid-template-columns` and `grid-template-rows`.\n- **Fractional Units (fr):** Grid introduces the powerful `fr` unit to proportionally distribute available space (e.g., `1fr 2fr` makes the second column twice as wide as the first).\n- **Grid Gap:** The `gap` property cleanly adds defined spacing between grid items across the board without dealing with complex margins.\n\nIt is incredibly powerful for dashboards, photo galleries, and complex page layouts!";
        } 
        
        // Match: "Give me ideas for a final year project"
        else if (text.includes('ideas for a final year project') || (text.includes('project') && text.includes('ideas'))) {
            return "Choosing a final year project is a great opportunity to showcase your skills. Here are three distinct, high-market-value ideas:\n\n### 1. AI-Powered Resume Analyzer\nA web app where users upload a PDF resume and a job description. The application uses machine learning to score the match percentage and suggest missing keywords.\n* **Tech:** React, Node.js, Python (FastAPI).\n\n### 2. Smart Campus Activity Tracker\nA mobile-friendly dashboard that tracks real-time crowd levels in libraries or cafeterias using Wi-Fi device density or simple optical AI monitoring securely.\n* **Tech:** Vue.js, Firebase, OpenCV.\n\n### 3. Real-Time Collaborative IDE\nA stripped-down browser code editor where multiple peers can type on the same document simultaneously, perfect for interviews or tutoring.\n* **Tech:** Next.js, WebSockets (Socket.io), and Monaco Editor.\n\nLet me know which domain (AI, Web, or Security) you prefer and I can tailor more ideas!";
        } 
        
        // Match: "Translate this text to Spanish"
        else if (text.includes('translate') && text.includes('spanish')) {
            return "I can certainly assist with Spanish translations! \n\nIf you click the generic suggestion card, you haven't provided specific text yet. Here is an example of my translation skills:\n\n* **English:** \"Education is important.\"\n* **Spanish:** *\"La educación es importante.\"*\n\nPlease reply with the exact text you want transcribed, and I will instantly return the Spanish translation!";
        }

        // ---------------------------------------------------------
        // Core Web Dev Topics (Fallbacks)
        // ---------------------------------------------------------
        else if (text === 'dom' || text.includes('document object model') || text.includes('the dom')) {
            return "Certainly! The **DOM (Document Object Model)** is a programming interface for web documents. It represents the structure of the page so that programs can change the document structure, style, and content dynamically.\n\n### How it works:\n- The DOM represents the document as a **tree of nodes** (such as `<html>`, `<body>`, and `<div>`).\n- JavaScript can interact with this tree to read, add, update, or delete elements.\n\n**Example:**\n```javascript\n// Select an element by ID and change its text content\ndocument.getElementById('myId').textContent = 'Hello, DOM!';\n```\n\nLet me know if you would like to see more advanced DOM manipulation techniques!";
        } else if (text.includes('flexbox') || text.includes('flex')) {
            return "I'd be happy to explain CSS Flexbox! **Flexbox (Flexible Box Layout)** is a CSS layout module designed to provide a highly efficient way to lay out, align, and distribute space among items in a container, even when their size is unknown.\n\n### Key Flexbox Concepts:\n- **`display: flex;`**: Defines a flex container.\n- **`justify-content`**: Aligns items horizontally along the main axis.\n- **`align-items`**: Aligns items vertically along the cross axis.\n\n**Quick Trick for Perfect Centering:**\n```css\n.container {\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n}\n```\n\nWould you like a detailed guide on using Flexbox versus CSS Grid?";
        } else if (text.includes('promise') || text.includes('promises') || text.includes('async')) {
            return "Of course! Let's discuss **JavaScript Promises**. A Promise represents the eventual completion (or failure) of an asynchronous operation, allowing you to handle operations like network requests gracefully.\n\n### The Three States of a Promise:\n1. **Pending**: The initial state; the operation has not completed yet.\n2. **Fulfilled**: The operation completed successfully.\n3. **Rejected**: The operation failed.\n\n**Example using `async/await`:**\n```javascript\nasync function fetchUserData() {\n    try {\n        const response = await fetch('https://api.example.com/user');\n        const data = await response.json();\n        console.log('User Data:', data);\n    } catch (error) {\n        console.error('Network Error:', error);\n    }\n}\n```\n\nAre you currently working on an API integration where you need to implement Promises?";
        } else if (text.includes('bootstrap') || text.includes('grid system')) {
            return "I can certainly help with that! **Bootstrap 5** features a powerful, mobile-first flexbox grid system for building layouts of all shapes and sizes.\n\n### How the Grid Works:\n- **Containers**: Wrap your grid using `.container` (fixed-width) or `.container-fluid` (full-width).\n- **Rows**: Use `.row` to create horizontal groups of columns.\n- **Columns**: Bootstrap uses a 12-column system. For example, `.col-md-6` takes up exactly half the width on medium-sized screens.\n\n**Example Responsive Layout:**\n```html\n<div class=\"container\">\n  <div class=\"row\">\n    <div class=\"col-12 col-md-8\">Main Content (8 columns)</div>\n    <div class=\"col-12 col-md-4\">Sidebar Content (4 columns)</div>\n  </div>\n</div>\n```\n\nLet me know if you need help designing a specific layout with Bootstrap!";
        }

        // ---------------------------------------------------------
        // General Tech Broad Matchers & Greetings
        // ---------------------------------------------------------
        else if (text === 'hi' || text === 'hello' || text === 'hey' || text.startsWith('good morning') || text.startsWith('good evening')) {
            return "Hello! How can I assist you today? I'm here to help you brainstorm ideas, write code, or explain complex concepts. What's on your mind?";
        } else if (text.includes('how are you')) {
            return "I'm functioning perfectly, thank you for asking! I'm ready to help you tackle whatever tasks or questions you have today. How can I assist you?";
        } else if (text.includes('who are you') || text.includes('what are you')) {
            return "I am an AI assistant designed to be helpful, harmless, and honest. I can generate code, summarize information, translate text, and help you brainstorm creative ideas. What would you like to work on?";
        } else if (text.includes('code') || text.includes('python') || text.includes('script') || text.includes('write')) {
            return "Certainly! Here is a robust Python script that demonstrates best practices, including type hinting and docstrings.\n\n```python\n# A simple function to greet a user\ndef greet_user(name: str) -> None:\n    \"\"\"\n    Prints a personalized greeting to the console.\n    \"\"\"\n    print(f'Hello, {name}! Welcome to the platform.')\n\n# Execute the function\nif __name__ == '__main__':\n    greet_user('World')\n```\n\n### Key Aspects of This Code:\n- **Type Hints:** Specifying `name: str` makes the code significantly more readable and easier to debug.\n- **Docstrings:** Adding brief documentation helps other developers understand the function's purpose.\n\nLet me know if you need any modifications or explanations for this snippet!";
        } else if (text.includes('summarize') || text.includes('summary')) {
            return "I'd be happy to help with that! Here is a concise summary of the core web technologies you might be studying:\n\n1. **HTML (HyperText Markup Language)**: Acts as the structural foundation and semantic meaning of a webpage.\n2. **CSS (Cascading Style Sheets)**: Handles the visual presentation, color schemes, typography, and responsive layouts.\n3. **JavaScript**: Adds interactivity, complex logic, and dynamic state management to front-end applications.\n\nPlease provide any specific text or article if you'd like me to summarize it directly for you.";
        } else if (text.includes('translate') || text.includes('translation')) {
            return "I can certainly help you with translation! I am trained to understand and translate numerous languages including Spanish, French, German, Mandarin, and many more.\n\nPlease provide the specific phrase or paragraph you would like me to translate, and indicate your target language.";
        } else if (text.match(/\bhtml\b/)) {
            return "**HTML (HyperText Markup Language)** forms the raw skeleton of any web application.\n\n### Modern HTML Practices:\n- **Semantic Elements:** Using `<header>`, `<nav>`, `<article>`, and `<footer>` improves SEO and accessibility.\n- **Forms:** HTML5 introduced advanced input types like `date`, `email`, and `range` with built-in browser validation.\n\nNeed an example of an accessible HTML5 form template?";
        } else if (text.match(/\bcss\b/) || text.includes('stylesheet')) {
            return "**CSS (Cascading Style Sheets)** brings your HTML to life with layout, color, and responsive design.\n\n### CSS Superpowers:\n- **CSS Variables:** Define global theme colors natively using `--primary-color: #007bff;`.\n- **Responsive Design:** Media queries (`@media`) allow layouts to seamlessly adapt to mobile devices.\n- **Animations:** You can use `@keyframes` to create buttery-smooth transitions and hover effects.\n\nDo you need help centering a div or building a custom Flexbox layout?";
        } else if (text.match(/\bjs\b/) || text.includes('javascript') || text.includes('ecmascript')) {
            return "**JavaScript** is the brain behind modern web interactivity.\n\n### Essential JS Concepts:\n- **The DOM:** JS allows you to target, modify, and style HTML elements dynamically.\n- **Events:** You can listen for user actions like `click` or `keyup` using `.addEventListener()`.\n- **Modern Syntax:** Modern JS (ES6+) uses `const/let`, arrow functions `() =>`, and Promises for much cleaner code.\n\nWould you like a snippet demonstrating how to build a dynamic counter?";
        } else if (text.includes('react') || text.includes('vue') || text.includes('framework')) {
            return "Frontend frameworks like **React**, **Vue**, and **Angular** have revolutionized web development!\n\nInstead of manually tracking DOM elements, these tools use a **Component-Based Architecture** and often a Virtual DOM to efficiently update only the parts of the UI that change. This makes building complex Single Page Applications (SPAs) significantly easier.\n\nAre you looking to learn a specific component framework for your next project?";
        } else if (text.match(/what is .*?\?/)) {
            return "That is an excellent question.\n\nWhile I am currently operating as a localized assistant without access to a comprehensive real-time database, I function by analyzing, synthesizing, and explaining complex topics ranging from computer science to natural history.\n\nIf you have specific questions about **programming paradigms**, **UI/UX design**, or **software engineering**, I can provide highly detailed mock examples for you. How can I assist you with those areas today?";
        } else if (text.match(/why .*?\?/)) {
            return "Understanding the \"why\" is arguably the most important part of learning! \n\nTypically, answering \"why\" involves analyzing underlying systems, historical technology context, or specific technical constraints. If you have a specific \"why\" question related to coding (e.g., \"Why use CSS Grid instead of Flexbox?\"), I would be more than happy to give you a comprehensive breakdown.";
        } else if (text.match(/how .*?\?/)) {
            return "I would be glad to explain how that works! \n\nNormally, I provide a clear, step-by-step guide breaking down any process from start to finish. If you need a tutorial on something specific, like \"how to vertically center a div\" or \"how to iterate through an object in JavaScript,\" please just let me know and I will generate the complete solution for you.";
        } else {
            return "I apologize, but I am not certain how to appropriately respond to that based on my current localized knowledge constraints. \n\nHowever, I am fully equipped to help you with several key topics:\n- **Writing and debugging code snippets** (Python, JavaScript, HTML/CSS)\n- **Brainstorming creative project ideas**\n- **Providing data summaries and structured advice**\n\nCould you please rephrase your request or let me know if you need help with one of the topics listed above?";
        }
    }

    // ==========================================
    // Core Functionality (Task 3)
    // ==========================================

    // Auto-resize Textarea
    $messageInput.on('input', function () {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';

        // Enable/Disable send button
        if ($(this).val().trim() !== '') {
            $sendBtn.removeAttr('disabled');
        } else {
            $sendBtn.attr('disabled', 'disabled');
        }
    });

    // Handle Enter / Shift+Enter
    $messageInput.on('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent new line
            if (!isWaitingForResponse && $(this).val().trim() !== '') {
                handleSend();
            }
        }
    });

    // Click Send Button
    $sendBtn.on('click', function (e) {
        e.preventDefault();
        if (!isWaitingForResponse) {
            handleSend();
        }
    });

    // Click Suggestion Cards
    $('.suggestion-card').on('click', function () {
        if (!isWaitingForResponse) {
            const suggestionText = $(this).find('p').text();
            $messageInput.val(suggestionText);

            // Trigger input event to resize textarea and enable send button
            $messageInput.trigger('input');

            // Optional: send immediately on click
            // handleSend(); 
        }
    });

    // Handle message sending flow
    function handleSend() {
        const text = $messageInput.val().trim();
        if (text === '') return;

        // Reset input
        $messageInput.val('');
        $messageInput.get(0).style.height = 'auto';
        $sendBtn.attr('disabled', 'disabled');

        // Hide welcome screen if first message
        if (isFirstMessage) {
            $welcomeScreen.hide();
            isFirstMessage = false;
        }

        // Add user message
        addMessage(text, 'user');

        // Play send sound (catch errors if browser blocks autoplay)
        if (sendSound) sendSound.play().catch(e => console.log('Audio play blocked:', e));

        isWaitingForResponse = true;

        // Show typing indicator
        showTypingIndicator();

        // Simulate AI delay (1-2 seconds)
        const delay = Math.floor(Math.random() * 1000) + 1000;
        setTimeout(() => {
            hideTypingIndicator();

            // Pick response based on user text
            const responseContent = getMockResponse(text);

            // Add AI message with typing animation
            addMessage(responseContent, 'ai', true);

            if (receiveSound) receiveSound.play().catch(e => console.log('Audio play blocked:', e));
            isWaitingForResponse = false;
        }, delay);
    }

    // Add message to DOM
    function addMessage(content, sender, animateTyping = false) {
        const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const avatarHtml = sender === 'user'
            ? `<div class="avatar bg-gradient-user"><span>S</span></div>`
            : `<div class="avatar bg-gradient-ai"><i class="fa-solid fa-robot"></i></div>`;

        const nameStr = sender === 'user' ? 'You' : 'Gen AI';

        // Setup message structure
        const $msgWrapper = $('<div>').addClass(`message ${sender}-message`);
        const $avatarContainer = $('<div>').addClass('message-avatar').html(avatarHtml);
        const $contentContainer = $('<div>').addClass('message-content');
        const $header = $('<div>').addClass('message-header').html(`<strong>${nameStr}</strong> &bull; ${timeStr}`);
        const $bubble = $('<div>').addClass('message-bubble');

        if (sender === 'ai' && animateTyping) {
            // Typing Animation logic (Bonus)
            $contentContainer.append($header).append($bubble);
            $msgWrapper.append($avatarContainer).append($contentContainer);
            $messagesContainer.append($msgWrapper);

            // Typewriter effect
            let i = 0;
            $bubble.html(''); // start empty
            scrollToBottom();

            function typeWriter() {
                if (i < content.length) {
                    // Update text, parse markdown for valid display during typing
                    const currentText = content.substring(0, i + 1);
                    if (window.marked) {
                        $bubble.html(window.marked.parse(currentText));
                    } else {
                        $bubble.text(currentText);
                    }
                    i++;
                    scrollToBottom();
                    setTimeout(typeWriter, 15); // typing speed
                }
            }
            typeWriter();
        } else {
            // Normal instant inject
            let finalOutput = content;
            if (sender === 'ai' && window.marked) {
                finalOutput = window.marked.parse(content);
            } else if (sender === 'user') {
                // escape html for user to prevent injection, wrap in standard text
                finalOutput = $('<div>').text(content).html();
                finalOutput = finalOutput.replace(/\n/g, '<br>');
            }

            $bubble.html(finalOutput);
            $contentContainer.append($header).append($bubble);
            $msgWrapper.append($avatarContainer).append($contentContainer);
            $messagesContainer.append($msgWrapper);
            scrollToBottom();
        }
    }

    function showTypingIndicator() {
        $typingIndicator.show();
        $messagesContainer.append($typingIndicator); // Move to bottom
        scrollToBottom();
    }

    function hideTypingIndicator() {
        $typingIndicator.hide();
    }

    function scrollToBottom() {
        $chatArea.scrollTop($chatArea[0].scrollHeight);
    }

    // ==========================================
    // Sidebar & Mobile (Task 4)
    // ==========================================

    $('#hamburgerMenu').on('click', function () {
        $sidebar.addClass('show');
        $sidebarOverlay.addClass('show');
    });

    $sidebarOverlay.on('click', function () {
        $sidebar.removeClass('show');
        $sidebarOverlay.removeClass('show');
    });

    $('#newChatBtn').on('click', function () {
        // Reset chat
        $messagesContainer.empty();
        $welcomeScreen.show();
        isFirstMessage = true;
        isWaitingForResponse = false;
        hideTypingIndicator();
        $messageInput.val('');
        $messageInput.get(0).style.height = 'auto';
        $sendBtn.attr('disabled', 'disabled');

        // Close sidebar on mobile
        if (window.innerWidth <= 768) {
            $sidebar.removeClass('show');
            $sidebarOverlay.removeClass('show');
        }
    });

    // ==========================================
    // Bonus Features
    // ==========================================

    // Dark Mode Toggle
    $('#themeToggle').on('click', function () {
        const theme = $('html').attr('data-theme');
        const icon = $(this).find('i');
        if (theme === 'light') {
            $('html').attr('data-theme', 'dark');
            icon.removeClass('fa-moon').addClass('fa-sun');
        } else {
            $('html').attr('data-theme', 'light');
            icon.removeClass('fa-sun').addClass('fa-moon');
        }
    });

    // Export Chat functionality
    $('#exportChatBtn').on('click', function () {
        if ($messagesContainer.children('.message:not(.typing-indicator-wrapper)').length === 0) {
            alert('No chat history to export!');
            return;
        }

        let chatText = "Gen AI Chat History\n\n";

        $messagesContainer.children('.message:not(.typing-indicator-wrapper)').each(function () {
            const sender = $(this).hasClass('user-message') ? "You" : "AI";
            const time = $(this).find('.message-header').text().split('•')[1]?.trim() || '';
            // For user messages, taking text content to avoid html tags
            // For AI messages, text() removes marked tags nicely for plain text export
            const content = $(this).find('.message-bubble').text().trim();

            chatText += `[${time}] ${sender}:\n${content}\n\n`;
        });

        // Create Blob
        const blob = new Blob([chatText], { type: "text/plain;charset=utf-8" });
        const url = URL.createObjectURL(blob);

        // Trigger download
        const a = document.createElement("a");
        a.href = url;
        a.download = "Gen_AI_Chat_Export.txt";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });
});