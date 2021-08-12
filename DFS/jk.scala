import scala.io.StdIn._


object Main extends App {
    val n = readInt
    val x = readInt
    var lowest_price = 2147483647
    var highest_price = 0
    for(i <- 0 until n) {
        val a = readInt
        val b = readInt
        val c = readInt
        val d = readInt
        
        var total_distance = a
        var total_cost = b
        
        while(total_distance <= x) {
            total_distance += c
            total_cost += d
        }
        lowest_price = math.min(lowest_price, total_cost)
        highest_price = math.max(highest_price, total_cost)
    }
            
    println(lowest_price + " " + highest_price)

}