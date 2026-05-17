// INDUSTRY DATA
const industryData = [
    {
        title: "Port Handling Equipment",
        desc: "Heavy-duty port machinery & specialized spare parts",
        items: [
            "Heavy-duty port equipment spare parts: spreaders, twistlocks, and crane components",
            "Genuine electrical and mechanical spare parts for ship-to-shore and yard operations",
            "Industrial instrumentation covering mechanical, hydraulic, and electrical port systems"
        ]
    },
    {
        title: "Oil & Gas Pumping Systems",
        desc: "Centrifugal & PD pumps, valves, flow control & safety",
        items: [
            "Centrifugal & positive displacement pump solutions for upstream, midstream, and downstream operations",
            "High-pressure systems: PSV valves, cylinder heads, turbochargers, gas main valves, and alternators",
            "Flow control & metering: gas flow meters, pressure switches, Rotork actuators, and ultrasonic flow measurement",
            "Pump repair kits, mechanical seals, gasket kits, bushings, and carbon fillers",
            "Ex-proof Warom lamps, flame arrestors, bursting disks, and overfill prevention controllers"
        ]
    },
    {
        title: "Instrumentation & Compressor Solutions",
        desc: "Air compressor components, rubber couplings & process control",
        items: [
            "Air compressor components: flexible rubber couplings, seals, gaskets, O-rings (NBR, EPDM, silicone)",
            "Anti-vibration mounts, isolator pads, and compressor dampers for industrial stability",
            "Compressor instrumentation: temperature control, pressure monitoring, and level indicators",
            "PLC, DCS, SCADA systems, robotics, and digital displays for modern process automation",
            "Compressor hose assemblies, silicone hoses, and hydraulic seals for demanding environments"
        ]
    },
    {
        title: "Electrical Parts & Solutions",
        desc: "Switchgears, VFDs, transformers & power distribution",
        items: [
            "Electrical actuators, MCCBs, soft starters, VFDs, and ATS (Automatic Transfer Switches)",
            "Control cabinets, switchgears, distribution transformers, and alternators",
            "Power quality: harmonic filters, capacitor banks, and power factor correction",
            "Armoured & unarmoured power cables, control cables, cable trays, and conduit systems"
        ]
    },
    {
        title: "Diesel Engines & Spare Parts",
        desc: "Premium engine components for heavy-duty & agricultural machinery",
        items: [
            "Premium diesel engine components: piston rings, cylinder liners, gasket kits, and turbochargers",
            "Coverage for Caterpillar, Cummins, Komatsu, Detroit Diesel, John Deere, Perkins, Case IH, Massey Ferguson, Volvo, and Yanmar",
            "Complete engine overhaul kits and individual replacement parts for construction, mining, agricultural, marine, and power generation sectors",
            "ISO 9001-certified quality standards — every component tested to OEM specifications"
        ]
    },
    {
        title: "Bearings & Power Transmission",
        desc: "Ball bearings, roller bearings, belts, pulleys & couplings",
        items: [
            "Deep groove ball bearings, angular contact, self-aligning, and spherical roller bearings",
            "Cylindrical, tapered, and needle roller bearings for high-load industrial applications",
            "Pillow blocks, flange units, plummer blocks, adapter sleeves, and lock nuts",
            "Power transmission: V-belts, timing belts, pulleys, sprockets, couplings, and transmission chains",
            "Stainless steel bearings, high-temperature bearings, and sealed bearings for harsh environments"
        ]
    },
    {
        title: "Water & Waste Water Industry",
        desc: "Industrial valves, pumps & treatment solutions",
        items: [
            "Industrial valves: butterfly, control, relief, check, gate, and non-return valves",
            "Pumps: submersible, sewage, deep well, multi-stage, booster, raw water, and vacuum pumps",
            "Water treatment equipment: filtration systems, chemical dosing, and UV disinfection"
        ]
    },
    {
        title: "Mining Solutions",
        desc: "Excavation, crushing, conveying & mineral processing",
        items: [
            "Heavy-duty excavation machinery: jaw, impact, and cone crushers, conveyors, and grinding equipment",
            "Conveyor components: polyester belts, tubular belts, heat-resistant belts, rollers, and garland idlers",
            "Instrumentation, mechanical, and electrical solutions tailored for mining operations",
            "Laboratory testing equipment, safety monitoring, and wear-resistant parts"
        ]
    },
    {
        title: "Gas & Industrial Products",
        desc: "Gas handling, safety systems & emission control",
        items: [
            "Air headers, distribution manifolds, and gas flow measurement systems",
            "Flame arrestors, bursting disks, fusible links, and fire protection for gas installations",
            "High-pressure ball valves, needle valves, forged DBB valves, and instrument manifolds",
            "Vapour recovery systems, vapour scrubber systems, and emission control equipment",
            "Tank equipment: overfill prevention controllers, mechanical level gauges, and portable liquid level sensors"
        ]
    },
    {
        title: "Filtration Industries",
        desc: "Oil, gas, fuel & industrial filtration systems",
        items: [
            "Filtration products from major manufacturers: Fleetguard, Donaldson, Terex, CAT, and Volvo",
            "Specialized filters: gas filters, carbon filters, fuel filters, oil filters, and air filters",
            "Coalescer/separator elements, activated carbon canisters, and cement bag filters",
            "Water treatment equipment filters and industrial filtration consumables"
        ]
    },
    {
        title: "Power Generation Industry",
        desc: "Hydro, thermal, wind & solar energy solutions",
        items: [
            "Core generation: hydropower plants, wind turbines, gas power plants, and solar energy systems",
            "Equipment & control: gas flow meters, industrial burners, boiler parts, gas main valves, and pressure switches",
            "Generators, turbines, alternators, and excitation systems",
            "Energy storage solutions: battery systems and smart energy management"
        ]
    },
    {
        title: "General Engineering",
        desc: "Starters, alternators, pumps & engineering support",
        items: [
            "Engine & hardware components: starters, alternators, valve guides, sensors, gasket kits, and adapters",
            "Advanced pumps: magnetic drive pumps, vane pumps, steam pumps, valve actuators, gasoline pumps, and micro pumps",
            "Industrial machinery equipment, engineering support analysis, and technical consultancy"
        ]
    }
];

function openIndustryModal(index) {
    const data = industryData[index];
    document.getElementById('industryModalTitle').textContent = data.title;
    document.getElementById('industryModalDesc').textContent = data.desc;
    const list = document.getElementById('industryModalList');
    list.innerHTML = '';
    data.items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        list.appendChild(li);
    });
    document.getElementById('industryModalOverlay').classList.add('open');
}

function closeIndustryModal() { document.getElementById('industryModalOverlay').classList.remove('open'); }
function closeIndustryModalOutside(e) { if (e.target === document.getElementById('industryModalOverlay')) closeIndustryModal(); }
