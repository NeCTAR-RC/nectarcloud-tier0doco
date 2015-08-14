## Consider Security

Security of your NeCTAR instances is your responsibility.

If we see evidence that an instance's security has been comprised, we
will take steps to shut down and isolate it so that it doesn't do any further
damage to cloud infrastructure or to other users' assets.

Compromised Nectar instances are a real issue. Across the Nectar federation, we
see examples at least once a month.

## Apply system patches as often as possible

Keeping your system up to date is one of the simplest and most effective
ways to secure your system against unwanted intrusion.

It is easy and more practical to configure a recent Linux system to apply
patches automatically.  Alternatively If you are applying patches by hand, we
recommend that you do it at least once a week.

## Understand the lifecycle of your Linux Distribution

Every release of a linux distribution (such as Debian Wheezy, or Ubuntu
Precise) will have a published end of life date.  Assuming you are doing the
right thing and applying patches regularly, once the end of life date is
reached, the patches will no longer be available.

If system patches are discontinued, you should update to a more recent version
of the operating system.  You should treat this as a matter of urgency.

It is trivially easy for a Bad Person(tm) to scan your machine and determine
exactly which attacks your instance is vulnerable to.

## Understand SSH authentication

It is undeniable that ssh key authentication is the most effective way to
secure ssh access to your instance.  Enabling ssh password authentication may
seem like a good idea, but doing so opens your machine to brute force password
attacks.  Don't underestimate the means and will of Bad People(tm) to exploit
your instance for their nefarious purposes.

Don't share your ssh private key with anyone, ever.   Like giving machine guns
to monkeys, it's a very bad idea.

## Don't use VNC, use x2go instead

VNC is one of those longstanding ways of getting graphical access to your
computer over a network.  While it's well known and loved, there are in fact
many ways to exploit VNC and there are now better ways to get to your graphical
content.

X2go is technically superior to VNC and tunnels your graphical content over
ssh.

## Terminate instances that you no longer require

In theory, you can run an instance as long as you like.  In practice, we would
prefer you to promptly terminate any instance that are not using actively, so
that other users can make use of the resources.

Currently, there is no formal Nectar mechanism to discourage wasteful use of
your allocation, but this is likely to change.

## What should I do when I am finished with an instance

When you are finished with an Instance, you should terminate it.  Leaving an
instance running, or in "paused" or "suspended" or "shutdown" states is tying
down resources that other people could be using.

Note that terminating an instance destroys its primary and ephemeral file
systems.  If you want to save the primary file system (so that you can launch a
new instance), snapshot the instance before you terminate it.
