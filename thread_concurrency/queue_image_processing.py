from multiprocessing import Process, Queue
import time


def process_images(queue):

    while not queue.empty():

        image = queue.get()

        print(f"Processing {image}")

        time.sleep(2)

        print(f"Finished {image}")


if __name__ == "__main__":

    queue = Queue()

    images = [
        "image1.jpg",
        "image2.jpg",
        "image3.jpg",
        "image4.jpg",
        "image5.jpg"
    ]

    # Put all images into queue
    for image in images:
        queue.put(image)

    workers = []

    # Create 3 worker processes
    for i in range(3):

        process = Process(
            target=process_images,
            args=(queue,)
        )

        workers.append(process)

        process.start()

    for process in workers:
        process.join()

    print("\nAll images processed.")