/**
 * Auto-updates the footer year.
 *
 * When the page finishes loading, this script finds the element
 * with the ID 'year' and inserts the current year into it.
 */
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('year').textContent = new Date().getFullYear();
});
