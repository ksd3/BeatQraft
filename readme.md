<div align=center>

<h1>BeatQraft</h1>

</div>

<h3 align=center>Are you a music producer who just can't quite find a beat? <span class="wave">&#128400</span>Do you need inspiration? Something that'll make your up-and-coming star the next Elvis? Fear not! The mysterious world of quantum mechanics is here to help!</h3>

To run this project locally make sure to be using Python3, install all the requirements, and then you can use start a local server by invoking the script `start.sh`:

```bash
pip install -r requirements.txt
bash start.sh
```

This project was presented at MIT iQuHACK-23, the international quantum computing hackathon hosted by and at MIT. It won **second place** at the IBM x Covalent Challenge, based on distributed and scalable quantum computing products using the covalent framework. 

Trained on 96 different types of beats (consisting of hi-hat, snare, and bass drums), this project produces a completely new beat generated by a Quantum Circuit Born Machine (QCBM) algorithm! These types of algorithms have been proven to be more expressive at scale, which was the aim of the problem. The project also selects beats after training by pulling a random number generated on the IBM Oslo Computer.

You can read the full report [here](https://github.com/ksd3/iQuHACK23-IBM-Covalent/blob/main/beatqraft/static/assets/docs/iQuHack_2023_Report.pdf).
