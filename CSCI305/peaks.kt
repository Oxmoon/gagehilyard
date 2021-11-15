/*
 * Kotlin Program for CSCI 305
 * Measures distance from Bozeman to mountain peaks by latitude and longitude
 * Returns lists and maps based on the questions
 *
 * Gage Hilyard
 */
 

// Data class to hold mountain peaks data

data class Peak(val name : String, val latitude : Double, val longitude : Double)

//inits list of peaks
//********Step One**********
fun listPeaks() : List<Peak>{
    val gaP = Peak(name = "Gallatin Peak", latitude = 45.3683,longitude = -111.3658)
    val grP = Peak(name = "Granite Peak", latitude = 45.1633, longitude = -109.8080)
    val whP = Peak(name = "Whitetail Peak", latitude = 45.0888, longitude = -109.5877)
    val pP = Peak(name = "Pikes Peak", latitude = 38.8409, longitude = -105.0423)
    val mP = Peak(name = "Mount Rainier", latitude = 46.879967, longitude = -121.726906)
    val peakList: MutableList<Peak> = mutableListOf(gaP, grP, whP, pP, mP)
    return peakList
}

//Given haversine formula, returns km
fun haversine(lat1: Double, lon1: Double, lat2: Double, lon2: Double): Double {
    val R = 6372.8 // in kilometers
    val l1 = Math.toRadians(lat1)
    val l2 = Math.toRadians(lat2)
    val dl = Math.toRadians(lat2 -lat1)
    val dr = Math.toRadians(lon2 -lon1)
    return 2 * R * Math.asin(Math.sqrt(Math.pow(Math.sin(dl / 2), 2.0) +Math.pow(Math.sin(dr / 2), 2.0) * Math.cos(l1) * Math.cos(l2)))
}

//Determines distance in km from Bozeman Montana of given peak
fun distanceFromBozeman(peak : Peak) : Double {
    val bozemanLat = 45.6770
    val bozemanLong = -111.0429
    return haversine(peak.latitude, peak.longitude, bozemanLat, bozemanLong)
    
}

fun main() {
    println("********Step Two**********")
    val peakLocations = listPeaks()
    peakLocations.forEach{println(it)}
    
    println("********Step Three**********")
    println("Distance from Whitetail: ${distanceFromBozeman(peakLocations[2])}")
    
    println("********Step Four**********")
    println("A new List with the distances of all Peaks in list to Bozeman")
    println("${peakLocations.map{distanceFromBozeman(it)}}")
    
    println("********Step Five**********")
    println("List of Peaks over 500KM from Bozeman")
    val farList : List<Peak> = peakLocations.filter{distanceFromBozeman(it)>=500}
    farList.forEach{println(it.name)}
    
    println("********Step Six**********")
    val bigTimberLong = -109.9541
    val westPeaks : List<Peak> = peakLocations.filter{it.longitude < bigTimberLong}
    val listNames : MutableList<String> = mutableListOf()
    westPeaks.map{listNames.add(it.name)}
    println("$listNames")
    
    println("********Step Seven**********")
    println("${peakLocations.maxByOrNull{it -> distanceFromBozeman(it)}}")
    
    println("********Step Eight**********")
    val mappedPeaks: Map<String, Peak> = peakLocations.associate { Pair(it.name, it) }
    mappedPeaks.forEach{
        k, v -> println("Name $k: Peak $v")
    }
    val key = "Gallatin Peak"
    if (mappedPeaks.containsKey(key)) {
        println("The latitude for Gallatin is ${mappedPeaks.getValue(key).latitude}")
    }
    
}