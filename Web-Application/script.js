function generateReport() {
    const input = document.getElementById('fileInput');
    const monthYear = document.getElementById('monthInput').value;
    if (!input.files[0]) {
        alert("Please upload a CSV file.");
        return;
    }

    const reader = new FileReader();
    reader.onload = function (event) {
        const csvData = event.target.result;
        processCSV(csvData, monthYear);
    };
    reader.readAsText(input.files[0]);
}

function processCSV(csvData, monthYear) {
    const rows = csvData.split('\n');
    let expenses = {};
    let totalExpenses = 0;

    rows.forEach(row => {
        const [item, price] = row.split(',');
        const count = prompt(`How many times did you buy ${item} in ${monthYear}?`, "0");
        const total = parseInt(count) * parseFloat(price);
        if (total > 0) {
            expenses[item] = total;
            totalExpenses += total;
        }
    });

    displayReport(expenses, totalExpenses, monthYear);
}

function displayReport(expenses, totalExpenses, monthYear) {
    let report = `Grocery Expenses for the month of "${monthYear}":<br>`;
    Object.keys(expenses).forEach(item => {
        report += `${item}: $${expenses[item].toFixed(2)}<br>`;
    });
    report += `Total Expenses: $${totalExpenses.toFixed(2)}`;
    document.getElementById('reportOutput').innerHTML = report;
}
