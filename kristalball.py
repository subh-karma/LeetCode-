var input = {"id":"SE1","data":10,"left":{"id":"SE2","data":12,"left":{"id":"SE4","data":4,"right":{"id":"SE8","data":9,"left":{"id":"SE15","data":20}}},"right":{"id":"SE5","data":17,"left":{"id":"SE9","data":10,"left":{"id":"SE16","data":8,"right":{"id":"SE17","data":18}}},"right":{"id":"SE10","data":11}}},"right":{"id":"SE3","data":7,"left":{"id":"SE6","data":6,"left":{"id":"SE11","data":18},"right":{"id":"SE12","data":2}},"right":{"id":"SE7","data":3,"left":{"id":"SE13","data":13},"right":{"id":"SE14","data":15}}}};

var lineWithHighestSales = function(data, bonus) {
    var line = [];
    var highestSalesLine = [];
    var highestSales = 0;

    function findHighestSalesLine(node, currentLine, currentSales) {
        if (!node) return;

        currentLine.push(node);
        currentSales += node.data;

        if (!node.left && !node.right) {
            if (currentSales > highestSales) {
                highestSales = currentSales;
                highestSalesLine = [...currentLine];
            }
        } else {
            findHighestSalesLine(node.left, currentLine, currentSales);
            findHighestSalesLine(node.right, currentLine, currentSales);
        }

        currentLine.pop();
    }

    findHighestSalesLine(data, [], 0);

    var totalSubordinates = highestSalesLine.length - 1;
    var budgetEfficiencyReward = bonus * 0.25;
    var salesEfficiencyReward = bonus * 0.75;

    for (var i = 0; i < highestSalesLine.length; i++) {
        var node = highestSalesLine[i];
        var subordinates = totalSubordinates - i;
        var budgetBonus = (subordinates / ((totalSubordinates * (totalSubordinates + 1)) / 2)) * budgetEfficiencyReward;
        var salesBonus = (node.data / highestSales) * salesEfficiencyReward;
        var totalBonus = Math.round(budgetBonus + salesBonus);

        line.push({
            id: node.id,
            bonus: totalBonus
        });
    }

    return line;
}

var bonus = 3000000;
var line = lineWithHighestSales(input, bonus);
console.log("Result :" + JSON.stringify(line));
var expectedLine = [{"id":"SE1","bonus":550000},{"id":"SE2","bonus":560000},{"id":"SE5","bonus":660000},{"id":"SE9","bonus":400000},{"id":"SE16","bonus":290000},{"id":"SE17","bonus":540000}];
console.log("Expected Result :" + JSON.stringify(expectedLine));