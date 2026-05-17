// PRODUCT DATA
const productData = [
    {
        title: "SKF / FAG / TIMKEN Bearings",
        image: "https://images.unsplash.com/photo-1565043589221-1a6fd9ae45c7?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/BEARI-PRODCT-300x300.jpg",
        desc: "Precision-engineered deep groove ball bearings, spherical roller bearings, tapered roller bearings, and cylindrical roller bearings from the world's most trusted bearing manufacturers — SKF, FAG, and TIMKEN. Designed for high-load, high-speed industrial applications across mining, power generation, manufacturing, and port operations.",
        specs: [
            "Deep Groove Ball Bearings (6000, 6200, 6300 series)",
            "Spherical Roller Bearings (22200, 22300 series)",
            "Tapered Roller Bearings (30200–33200 series)",
            "Cylindrical Roller Bearings (NU, NJ, NUP series)",
            "Sealed & shielded variants for harsh environments",
            "Bore diameters from 10 mm to 500 mm+"
        ],
        brands: ["SKF", "FAG", "TIMKEN"],
        category: "Bearings & Power Transmission"
    },
    {
        title: "Grundfos / LEWA Industrial Pumps",
        image: "https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/terex-backhoe-loader-hydraulic-pump-300x300-1.jpg",
        desc: "High-performance centrifugal, positive displacement, metering, and diaphragm pumps from Grundfos and LEWA. Built for upstream, midstream, and downstream oil & gas operations, chemical processing, water treatment, and industrial fluid handling. Engineered for reliability under extreme pressure, temperature, and corrosive conditions.",
        specs: [
            "Grundfos CR/CRN multistage centrifugal pumps",
            "LEWA ecoflow diaphragm metering pumps",
            "Grundfos SP submersible borehole pumps",
            "Flow rates from 0.1 to 500 m³/h",
            "Pressure ratings up to PN 400 (400 bar)",
            "ATEX-certified ex-proof variants available"
        ],
        brands: ["Grundfos", "LEWA"],
        category: "Oil & Gas Pumping Systems"
    },
    {
        title: "WIKA / Emerson Process Instruments",
        image: "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/abb_b_family-300x300-1.png",
        desc: "Comprehensive range of industrial instrumentation from WIKA and Emerson for pressure, temperature, flow, and level measurement. Seamless integration with PLC, DCS, and SCADA systems for modern process automation in oil & gas, chemical, power generation, and water treatment facilities.",
        specs: [
            "WIKA pressure gauges, transmitters & diaphragm seals",
            "Emerson Rosemount temperature transmitters",
            "WIKA thermowells & RTD/thermocouple sensors",
            "Emerson Coriolis, magnetic & vortex flow meters",
            "Level measurement: radar, ultrasonic & float switches",
            "HART, Foundation Fieldbus, Profibus communication"
        ],
        brands: ["WIKA", "Emerson"],
        category: "Instrumentation & Compressor Solutions"
    },
    {
        title: "Schneider / Siemens Switchgears & VFDs",
        image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/stater.jpg",
        desc: "Complete electrical distribution and motor control solutions from Schneider Electric and Siemens. Switchgears, MCCBs, VFDs, soft starters, ATS, control cabinets, and distribution transformers for industrial plants, commercial buildings, and infrastructure projects across East Africa.",
        specs: [
            "Schneider Masterpact / Compact NSX MCCBs",
            "Siemens SENTRON 3VA / 3WL air circuit breakers",
            "Schneider Altivar / Siemens SINAMICS VFDs",
            "Soft starters: Altistart 22 / SIRIUS 3RW",
            "Automatic Transfer Switches (ATS) 63A–3200A",
            "Power factor correction & harmonic filtering"
        ],
        brands: ["Schneider Electric", "Siemens"],
        category: "Electrical Parts & Solutions"
    },
    {
        title: "Cummins / CAT / Volvo Engine Kits",
        image: "https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/mechanical-1.png",
        desc: "Premium diesel engine components and complete overhaul kits for Caterpillar, Cummins, Volvo Penta, Komatsu, Detroit Diesel, John Deere, Perkins, and more. Every component manufactured to ISO 9001-certified OEM specifications for construction, mining, agricultural, marine, and power generation sectors.",
        specs: [
            "Complete engine overhaul kits (pistons, rings, liners, gaskets)",
            "Turbochargers: Holset, Garrett, BorgWarner replacements",
            "Cylinder heads, valves, valve guides & seats",
            "Fuel injectors & injection pumps (Bosch, Delphi, Denso)",
            "Oil & water pumps, thermostats, belts & tensioners",
            "Coverage: CAT C-series, Cummins ISX/QSK, Volvo D-series"
        ],
        brands: ["Cummins", "Caterpillar", "Volvo", "Komatsu", "John Deere", "Perkins"],
        category: "Diesel Engines & Spare Parts"
    },
    {
        title: "SKF / Timken Power Transmission",
        image: "https://images.unsplash.com/photo-1537462715879-360eeb61a0ad?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/electric_motor_cropped-300x300.jpg",
        desc: "Comprehensive power transmission solutions from SKF and Timken — V-belts, timing belts, pulleys, sprockets, flexible couplings, transmission chains, and locking devices. Engineered for reliable torque transfer in conveyors, crushers, pumps, compressors, and heavy rotating machinery.",
        specs: [
            "SKF PHG V-belts (classical, wedge, cogged)",
            "SKF Power Transmission timing belts (HTD, STD profiles)",
            "SKF taper bush & QD bushing pulleys",
            "Sprockets: simplex, duplex, triplex (ISO 606)",
            "Transmission & conveyor chains (08B–32B series)",
            "SKF Grid, Gear, and Jaw flexible couplings"
        ],
        brands: ["SKF", "Timken"],
        category: "Bearings & Power Transmission"
    },
    {
        title: "Xylem / Flygt Submersible Pumps",
        image: "https://images.unsplash.com/photo-1541844053589-346841d0b34c?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/flow-meters.jpg",
        desc: "Reliable submersible, sewage, drainage, and dewatering pumps from Xylem and its Flygt brand — the global benchmark in wastewater handling. Together with Grundfos booster and multistage pumps, we cover the full water cycle from abstraction to treatment and distribution.",
        specs: [
            "Flygt N-series submersible wastewater pumps",
            "Flygt B-series dewatering & drainage pumps",
            "Grundfos CR/CM booster & multistage pumps",
            "Mixers & aerators for treatment plants",
            "Industrial valves: gate, butterfly, check, control",
            "Monitoring & control: SCADA-ready pump controllers"
        ],
        brands: ["Xylem", "Flygt", "Grundfos"],
        category: "Water & Waste Water"
    },
    {
        title: "Caterpillar / Komatsu Mining Equipment",
        image: "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/12/mining.jpg",
        desc: "Heavy-duty mining machinery and spare parts from Caterpillar and Komatsu — the two largest mining equipment manufacturers globally. We supply parts for excavators, bulldozers, haul trucks, crushers, conveyor systems, and drilling equipment for surface and underground mining operations.",
        specs: [
            "CAT 6015/6020 hydraulic mining shovels parts",
            "Komatsu D375/D475 dozer undercarriage components",
            "Jaw, cone & impact crusher wear parts (mantles, liners)",
            "Conveyor belts: polyester, steel cord, heat-resistant",
            "Garland & impact idlers, return rollers, belt fasteners",
            "GET (Ground Engaging Tools): teeth, adapters, shrouds"
        ],
        brands: ["Caterpillar", "Komatsu", "Terex"],
        category: "Mining Solutions"
    },
    {
        title: "Rotork / Honeywell Gas Safety Systems",
        image: "https://images.unsplash.com/photo-1518152006812-edab29b069ac?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/abb_b_family-300x300-1.png",
        desc: "Mission-critical gas handling and safety equipment from Rotork, Honeywell, Endress+Hauser, and Klinger. Valve actuators, gas flow meters, flame arrestors, bursting disks, overfill prevention systems, vapour recovery, and emission control for gas terminals, refineries, and petrochemical plants.",
        specs: [
            "Rotork IQ3 / CVA electric & pneumatic valve actuators",
            "Honeywell Searchpoint / XNX gas detectors",
            "Endress+Hauser Proline gas flow meters (ultrasonic & Coriolis)",
            "Elmac / PROTEGO flame arrestors & breather valves",
            "ZOOK / BS&B bursting disks & rupture panels",
            "Scully overfill prevention & tank level monitoring"
        ],
        brands: ["Rotork", "Honeywell", "Endress+Hauser", "Klinger"],
        category: "Gas & Industrial Products"
    },
    {
        title: "Donaldson / Fleetguard Filtration",
        image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/tower_light-removebg-preview-300x300-1.png",
        desc: "Industry-leading filtration solutions from Donaldson and Fleetguard (Cummins Filtration) — the two most trusted names in industrial filtration. Oil filters, fuel filters, air filters, gas filters, hydraulic filters, and coalescer/separator elements for engines, compressors, turbines, and process systems.",
        specs: [
            "Donaldson PowerCore / RadialSeal air filters",
            "Fleetguard LF/FF series lube & fuel filters",
            "Donaldson P-Series hydraulic & bulk oil filtration",
            "Coalescer/separator elements (oil/water separation)",
            "Gas filter cartridges, carbon canisters & bag filters",
            "Cross-reference: Fleetguard, Donaldson, CAT, Volvo, Terex"
        ],
        brands: ["Donaldson", "Fleetguard", "Cummins Filtration"],
        category: "Filtration Industries"
    },
    {
        title: "Mecc Alte / Siemens Power Generation",
        image: "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/mechanical-1.png",
        desc: "Complete power generation solutions from Mecc Alte alternators to Siemens turbines and generators. Covering hydro, thermal, wind, and solar energy systems — plus industrial burners, boiler parts, gas flow meters, pressure switches, and energy storage solutions for on-grid and off-grid applications.",
        specs: [
            "Mecc Alte ECP/ECO series alternators (5–4000 kVA)",
            "Siemens SGT industrial gas turbines",
            "Cummins / Perkins diesel generator sets",
            "Solar inverters & battery energy storage systems",
            "Industrial burners & boiler pressure parts",
            "Synchronization panels & excitation systems"
        ],
        brands: ["Mecc Alte", "Siemens", "Cummins"],
        category: "Power Generation"
    },
    {
        title: "Konecranes / Terex Port Solutions",
        image: "https://images.unsplash.com/photo-1590243677335-900508603610?w=800&q=85",
        fallback: "https://www.ipatechs.com/wp-content/uploads/2024/11/terex-backhoe-loader-hydraulic-pump-300x300-1.jpg",
        desc: "Heavy-duty port handling equipment and spare parts from Konecranes and Terex — two of the world's leading port machinery manufacturers. Ship-to-shore gantry cranes, rubber-tyred gantry cranes, reach stackers, spreaders, twistlocks, and yard handling equipment for container terminals across East Africa.",
        specs: [
            "Konecranes STS & RTG crane components",
            "Terex / Fantuzzi reach stacker parts",
            "Container spreaders: fixed & telescopic (20–40 ft)",
            "Twistlock assemblies, flippers & landing pins",
            "Wire rope, sheaves, wheels, brakes & drives",
            "Electrical & hydraulic systems for port equipment"
        ],
        brands: ["Konecranes", "Terex", "Fantuzzi"],
        category: "Port Handling Equipment"
    }
];

function openProductDetail(index) {
    const data = productData[index];
    document.getElementById('productDetailImage').src = data.image;
    document.getElementById('productDetailImage').onerror = function () { this.src = data.fallback; };
    document.getElementById('productDetailTitle').textContent = data.title;
    document.getElementById('productDetailCat').textContent = data.category;
    document.getElementById('productDetailDesc').textContent = data.desc;
    const list = document.getElementById('productDetailSpecs');
    list.innerHTML = '';
    data.specs.forEach(spec => {
        const li = document.createElement('li');
        li.textContent = spec;
        list.appendChild(li);
    });
    const brandsEl = document.getElementById('productDetailBrands');
    brandsEl.innerHTML = '';
    data.brands.forEach(brand => {
        const span = document.createElement('span');
        span.className = 'product-brand-tag';
        span.textContent = brand;
        brandsEl.appendChild(span);
    });
    document.getElementById('productDetailOverlay').classList.add('open');
}

function closeProductDetail() { document.getElementById('productDetailOverlay').classList.remove('open'); }
function handleProductOverlayClick(e) { if (e.target === document.getElementById('productDetailOverlay')) closeProductDetail(); }

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeProductDetail();
});
