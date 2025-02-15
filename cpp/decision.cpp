#include <iostream>
#include <vector>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

struct StockData {
    std::string date;
    double open;
    double close;
    double high;
    double low;
    double volume;
};

double calculateSMA(const std::vector<StockData>& data, int period) {
    if (data.size() < period) return -1;
    double sum = 0;
    for (int i = data.size() - period; i < data.size(); i++) {
        sum += data[i].close;
    }
    return sum / period;
}

std::string makeDecision(const std::vector<StockData>& data) {
    double sma_20 = calculateSMA(data, 20);
    double sma_50 = calculateSMA(data, 50);

    if (sma_20 == -1 || sma_50 == -1) return "Not enough data";
    return (sma_20 > sma_50) ? "BUY" : "SELL";
}

int main() {
    std::string jsonData = R"([{"date":"2024-02-12","open":150,"close":155,"high":157,"low":149,"volume":1000000},
                               {"date":"2024-02-13","open":156,"close":158,"high":160,"low":154,"volume":900000}])";

    std::vector<StockData> stockData;
    json parsedData = json::parse(jsonData);

    for (auto& item : parsedData) {
        stockData.push_back({item["date"], item["open"], item["close"], item["high"], item["low"], item["volume"]});
    }

    std::string decision = makeDecision(stockData);
    std::cout << decision << std::endl;
    return 0;
}
