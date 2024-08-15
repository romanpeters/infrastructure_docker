import os
import sys
import yaml

def extract_first_service_and_port(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    services = data.get('services', {})
    if services:
        first_service_name, first_service_info = next(iter(services.items()))
        ports = first_service_info.get('ports', [])
        if ports:
            host_port = ports[0].split(':')[0]
            return (first_service_name, int(host_port))
    return None

def main(output_file=None):
    base_dir = '.'  # Adjust this if your directory is different
    all_services_ports = []
    for root, dirs, files in os.walk(base_dir):
        if 'docker-compose.yml' in files:
            file_path = os.path.join(root, 'docker-compose.yml')
            service_port = extract_first_service_and_port(file_path)
            if service_port:
                all_services_ports.append(service_port)
    
    all_services_ports.sort(key=lambda x: x[1])  # Sort by port number
    
    output = '\n'.join(f"{port} {service_name}" for service_name, port in all_services_ports) + '\n'
    
    if output_file:
        with open(output_file, 'w') as file:
            file.write(output)
    
    print(output)

if __name__ == '__main__':
    output_file = sys.argv[1] if len(sys.argv) > 1 else None
    main(output_file)

