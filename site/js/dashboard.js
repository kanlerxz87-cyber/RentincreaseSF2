// Dashboard interactivity script
document.addEventListener('DOMContentLoaded', () => {
    console.log('Rental Increase SF Dashboard loaded.');
    
    // Add hover effects to table rows
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(row => {
        row.addEventListener('mouseenter', () => row.style.backgroundColor = '#f1f1f1');
        row.addEventListener('mouseleave', () => row.style.backgroundColor = '');
    });

    // Add click feedback to navigation links
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            console.log(`Navigating to: ${link.href}`);
        });
    });
});