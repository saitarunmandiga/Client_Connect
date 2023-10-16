// This JS file is to help retrieve and save user preferences

// Function to fetch saved preferences
function fetchPreferences(userId) {
    fetch(`/getPreferences/${userId}`)
    .then(response => response.json())
    .then(data => {
        // Use this data to rearrange widgets or hide/show them as per saved preferences
        let widgetOrder = JSON.parse(data.widget_order);
        let widgetVisibility = JSON.parse(data.widget_visibility);
        
        // Handle reordering and visibility of widgets based on the above
        // For example: 
        // reorderWidgets(widgetOrder);
        // setWidgetVisibility(widgetVisibility);
    });
}

// Function to save current preferences
function savePreferences(userId, widgetOrder, widgetVisibility) {
    let payload = {
        user_id: userId,
        widget_order: JSON.stringify(widgetOrder),
        widget_visibility: JSON.stringify(widgetVisibility)
    };

    fetch('/savePreferences', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
        } else {
            alert("Failed to save preferences. Please try again.");
        }
    });
}

// We will call these functions in appropriate events on frontend, 
// like when the user drags a widget or toggles its visibility.
