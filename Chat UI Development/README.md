# CampusPe Gen AI Chat UI

This project is a modern, responsive chat user interface similar to Claude or ChatGPT, built for the CampusPe Assignment.

## Technologies Used
- HTML5
- CSS3 (with Custom Properties / Variables)
- Vanilla JavaScript & jQuery
- Bootstrap 5 (for Grid handling and utility classes)
- Font Awesome (for icons)
- Google Fonts (Inter)
- Marked.js (Bonus: for rendering Markdown responses)

## Features Included
**Task 1: HTML Structure and Basic Layout**
- Semantic HTML tags used appropriately.
- Responsive layout including welcome screen and input areas.

**Task 2: CSS Styling and Design**
- Variable-based color theming (Light and Dark modes).
- Clean, gradient-driven message bubbles.
- Typing animations (bouncing dots) and smooth transition hover effects.

**Task 3: JavaScript and jQuery Functionality**
- Message display with dynamic DOM injection.
- Dynamic auto-resizing input field.
- Handling of Enter to send, and Shift+Enter for newline.
- Simulated 1-2 second AI delay before providing responses from a mock array.

**Task 4: Sidebar and Advanced Features**
- Collapsible sidebar on mobile devices (hamburger menu logic).
- Overlay mask applied to body dynamically on smaller screens.
- Chat history listing UI.

### Bonus Features Implemented
- **Dark Mode Toggle**: A seamless mechanism for switching the app theme to a dark aesthetic.
- **Message Formatting**: Responses from AI support Markdown (links, code blocks, bold, italics).
- **Typing Animation**: AI types out its responses character by character instead of immediately popping in.
- **Chat Export**: Ability to download the current conversation's context into a plain text file.
- **Custom Scrollbar**: Modern styled scrollbar with reduced width and hover states.
- **Sound Effects**: Audio cues for sending and receiving messages.

## Setup Instructions

1. Simply open `index.html` in your choice of a modern Web Browser.
2. Ensure you have an internet connection, as the project relies on CDNs for Bootstrap, jQuery, FontAwesome, and Marked.js to work.

## Structure
```text
/
├── index.html        # Main HTML layout
├── css/
│   └── style.css     # The styling implementation
├── js/
│   └── chat.js       # Required functionality (UI binding + mocks)
└── README.md         # You are here
```

No build step or external backend is required! Enjoy!
