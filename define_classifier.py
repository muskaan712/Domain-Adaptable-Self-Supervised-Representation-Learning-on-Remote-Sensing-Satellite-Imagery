import torch
from config import DEVICE
from optimizer import LARS
import torch.nn as nn
from torch import optim
from define_simclr import simclr_model
from classifier import LinearEvaluation
from downstream_dataloader import nu_classes
simclr_model.load_state_dict(torch.load('simclr_resnet50_pre_two_stage_11')) #load_tar
eval_model = LinearEvaluation(simclr_model, nu_classes).to(DEVICE)
criterion = nn.CrossEntropyLoss().to(DEVICE)
optimizer = LARS(eval_model.parameters(), lr=0.005, momentum=0.9,  weight_decay=1e-6, nesterov=True)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=1000)