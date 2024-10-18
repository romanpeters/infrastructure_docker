import os
import sys
import yaml


def extract_first_service_and_port(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    services = data.get("services", {})
    if services:
        first_service_info = next(iter(services.values()))
        ports = first_service_info.get("ports", [])
        if ports:
            host_port = ports[0].split(":")[0]
            return int(host_port)
    return None


def main(output_file=None):
    base_dir = "."  # Adjust this if your directory is different
    all_services = []
    processed_paths = set()

    for root, dirs, files in os.walk(base_dir):
        if "docker-compose.yml" in files:
            file_path = os.path.join(root, "docker-compose.yml")
            if file_path not in processed_paths:
                port = extract_first_service_and_port(file_path)
                if port:
                    # Image name is the outer directory, container name is the inner directory
                    path_parts = root.split(os.sep)
                    image_name = path_parts[-2] if len(path_parts) > 1 else "."
                    container_name = path_parts[-1]
                    all_services.append((port, image_name, container_name, file_path))
                    processed_paths.add(file_path)

    all_services.sort(key=lambda x: x[0])

    output = (
        "\n".join(
            f"{port} {image} {container} {filename}"
            for port, image, container, filename in all_services
        )
        + "\n"
    )

    if output_file:
        with open(output_file, "w") as file:
            file.write(output)

    print(output)


if __name__ == "__main__":
    output_file = sys.argv[1] if len(sys.argv) > 1 else None
    main(output_file)

