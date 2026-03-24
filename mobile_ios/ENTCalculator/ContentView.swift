import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                NavigationLink(destination: PTACalculatorView()) {
                    Text("Pure Tone Average")
                }
                NavigationLink(destination: SNOT22View()) {
                    Text("SNOT-22 Score")
                }
            }
            .navigationTitle("ENT Toolkit")
        }
    }
}

struct PTACalculatorView: View {
    @State private var left500 = ""
    @State private var left1000 = ""
    @State private var left2000 = ""
    
    var body: some View {
        Form {
            Section(header: Text("Left Ear")) {
                TextField("500 Hz", text: $left500)
                TextField("1000 Hz", text: $left1000)
                TextField("2000 Hz", text: $left2000)
            }
            Button("Calculate") { }
        }
        .navigationTitle("PTA")
    }
}

struct SNOT22View: View {
    var body: some View {
        Text("SNOT-22 Interface")
            .navigationTitle("SNOT-22")
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
